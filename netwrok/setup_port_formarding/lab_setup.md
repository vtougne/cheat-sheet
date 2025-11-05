# Lab Setup Procedure

## Table of Contents

1. [Install / setup bind9 listening on my-berry](#1-install--setup-bind9-listening-on-my-berry) ✅
2. [Setup Windows desktop to use mini-buntu-admin as main DNS](#2-setup-windows-desktop-to-use-mini-buntu-admin-as-main-dns) 🔄
3. [Install basic web server listening on 8080 on mini-buntu network card](#3-install-basic-web-server-listening-on-8080-on-mini-buntu-network-card) ✅
4. [Setup DNS to make my-app:8080 targeting mini-buntu:8080](#4-setup-dns-to-make-my-app8080-targeting-mini-buntu8080) ✅
5. [Plan to be able to address http://my-app targeting mini-buntu:8080](#5-plan-to-be-able-to-address-httpmy-app-targeting-mini-buntu8080) ✅

## 1. setup DNS
### 1.1 Install / setup bind9 listening on my-berry

```bash
# Install BIND9
sudo apt update && sudo apt install bind9 bind9utils bind9-doc

# Validate configuration
sudo named-checkconf

# Service management
sudo systemctl start bind9
sudo systemctl restart bind9
sudo systemctl status bind9

# View logs
sudo journalctl -u bind9 -f

# Test DNS resolution
nslookup google.com 192.168.1.24
```

### 1.2 Open DNS port #53 on my-berry

```
  # SSH to my-berry
  ssh vince@my-berry

  # Check current firewall status
  sudo ufw status

  # Open port 53 for DNS (both TCP and UDP)
  sudo ufw allow 53/tcp
  sudo ufw allow 53/udp

  # If UFW is not enabled, enable it
  sudo ufw enable

  # Verify the rules
  sudo ufw status numbered

● After opening the port, test DNS accessibility:

  # Test DNS from another machine on your network
  nslookup google.com 192.168.1.24

  # Check if BIND9 is listening on port 53
  sudo netstat -tulpn | grep :53

  # Test from the raspberry itself
  dig @localhost google.com
  ```

### 1.3 Add DNS entry

Configure BIND9 to resolve `my-app` to `mini-buntu` (192.168.1.32):

```bash
# SSH to my-berry
ssh vince@my-berry

# Edit the BIND9 zone file (assuming zone is home.local)
sudo nano /etc/bind/db.home.local

# Add the following A record:
my-app          IN    A    192.168.1.32

# If zone file doesn't exist, create it first:
sudo cp /etc/bind/db.local /etc/bind/db.home.local

# Edit named.conf.local to include the zone
sudo nano /etc/bind/named.conf.local

# Add zone configuration:
zone "home.local" {
    type master;
    file "/etc/bind/db.home.local";
};

# Update the zone file with proper records
sudo nano /etc/bind/db.home.local
```

Example zone file content:
```
$TTL    604800
@       IN      SOA     my-berry.home.local. admin.home.local. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      my-berry.home.local.
@       IN      A       192.168.1.24
my-berry        IN      A       192.168.1.24
mini-buntu      IN      A       192.168.1.32
mini-buntu-admin IN     A       192.168.1.34
my-app          IN      A       192.168.1.32
```

```bash
# Check configuration
sudo named-checkconf
sudo named-checkzone home.local /etc/bind/db.home.local

# Restart BIND9
sudo systemctl restart bind9

# Test the DNS resolution
nslookup my-app.home.local 192.168.1.24
dig @192.168.1.24 my-app.home.local
```

## 3. Setup Port Forwarding
### 3.1 Install nginx on my-berry

```bash
# SSH to my-berry
ssh vince@my-berry

# Install nginx
sudo apt update && sudo apt install nginx -y

# Check nginx status
sudo systemctl status nginx
```

### 3.2 Configure nginx reverse proxy for my-app.home.local

```bash
# Create nginx site configuration for my-app
sudo tee /etc/nginx/sites-available/my-app <<EOF
server {
    listen 80;
    server_name my-app.home.local;

    location / {
        proxy_pass http://192.168.1.32:8080;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

# Enable the site
sudo ln -s /etc/nginx/sites-available/my-app /etc/nginx/sites-enabled/

# Test nginx configuration
sudo nginx -t

# Reload nginx
sudo systemctl reload nginx
```

### 3.3 Update DNS to point my-app.home.local to my-berry

```bash
# SSH to my-berry
ssh vince@my-berry

# Update the DNS record to point my-app to my-berry (not mini-buntu)
sudo sed -i 's/my-app.*IN.*A.*192.168.1.32/my-app          IN    A    192.168.1.24/' /etc/bind/db.home.local

# Reload BIND9
sudo systemctl reload bind9

# Test DNS resolution
nslookup my-app.home.local 192.168.1.24
```

### 3.4 Test the reverse proxy

```bash
# Test direct connection to mini-buntu:8080
curl -I http://192.168.1.32:8080

# Test reverse proxy through my-app.home.local
curl -I http://my-app.home.local

# Test full content
curl http://my-app.home.local
```

**Result**: `http://my-app.home.local:80` now successfully redirects to `http://mini-buntu:8080` through the nginx reverse proxy on my-berry.


### 3.5 Configure DNS forwarding and device discovery

#### 3.5.1 Configure BIND9 forwarding on my-berry

```bash
# SSH to my-berry
ssh vince@my-berry

# Edit BIND9 main config to forward unknown queries to Livebox
sudo tee /etc/bind/named.conf.options > /dev/null << 'EOF'
options {
    directory "/var/cache/bind";

    forwarders {
        192.168.1.1;    # Your Livebox
        8.8.8.8;        # Google DNS as backup
    };

    dnssec-validation auto;
    listen-on-v6 { any; };
};
EOF

# Remove reverse DNS zone to allow forwarding
sudo sed -i '/zone "1.168.192.in-addr.arpa"/,/};/d' /etc/bind/named.conf.local
sudo rm -f /etc/bind/db.192.168.1

# Check configuration and restart
sudo named-checkconf
sudo systemctl restart bind9
```

#### 3.5.2 Final BIND9 configurations

**Current /etc/bind/named.conf.options:**
```
options {
    directory "/var/cache/bind";

    forwarders {
        192.168.1.1;
        8.8.8.8;
    };

    dnssec-validation auto;
    listen-on-v6 { any; };
};
```

**Current /etc/bind/named.conf.local:**
```
//
// Do any local configuration here
//

// Consider adding the 1918 zones here, if they are not used in your
// organization
//include "/etc/bind/zones.rfc1918";


zone "home.local" {
    type master;
    file "/etc/bind/db.home.local";
};
```

#### 3.5.3 Network device discovery solution

Since BIND9 DNS forwarding doesn't work well for reverse DNS zones, use nmap with specific DNS servers for complete device discovery:

```bash
# To see all device names including Livebox devices:
nmap -sn --dns-servers 192.168.1.1 192.168.1.0/24

# Create an alias for convenience:
alias nmapscan='nmap -sn --dns-servers 192.168.1.1 192.168.1.0/24'

# Example output:
# Nmap scan report for livebox.home (192.168.1.1)
# Nmap scan report for chromecast.home (192.168.1.10)
# Nmap scan report for mcb.home (192.168.1.12)
# Nmap scan report for yoda.home (192.168.1.14)
# Nmap scan report for my-berry.home (192.168.1.24)
# Nmap scan report for mini-buntu.home (192.168.1.32)
# Nmap scan report for mini-buntu-admin.home (192.168.1.34)
```

**Note**: This approach gives you the best of both worlds:
- Your custom DNS entries (my-app.home.local, etc.) work through my-berry
- Complete device discovery shows all names through the Livebox DNS





## 3. Setup Windows desktop to use my-berry as main DNS
```
Pour configurer Windows pour utiliser mini-buntu-admin (192.168.1.34) comme serveur DNS :

  Méthode 1: Interface graphique

  1. Ouvrir les paramètres réseau :
  - Clic droit sur l'icône réseau → "Ouvrir les paramètres réseau et Internet"
  - Ou Windows + I → Réseau et Internet

  2. Modifier les paramètres de l'adaptateur :
  - Cliquer sur "Modifier les options d'adaptateur"
  - Clic droit sur votre connexion réseau → "Propriétés"

  3. Configurer IPv4 :
  - Sélectionner "Protocole Internet version 4 (TCP/IPv4)" → "Propriétés"
  - Cocher "Utiliser l'adresse de serveur DNS suivante"
  - Serveur DNS préféré : 192.168.1.34
  - Serveur DNS auxiliaire : 8.8.8.8 (optionnel, en backup)

  Méthode 2: PowerShell (admin)

  # Identifier l'interface réseau
  Get-NetAdapter

  # Configurer le DNS
  Set-DnsClientServerAddress -InterfaceAlias Wi-Fi -ServerAddresses "192.168.1.24","8.8.8.8"

  # Vérifier la configuration
  Get-DnsClientServerAddress

  Méthode 3: CMD (admin)

  # Configurer le DNS
  netsh interface ip set dns "Connexion au réseau local" static 192.168.1.34

  # Ajouter un DNS secondaire
  netsh interface ip add dns "Connexion au réseau local" 8.8.8.8 index=2

  Test de la configuration

  # Vider le cache DNS
  ipconfig /flushdns

  # Tester la résolution
  nslookup google.com 192.168.1.34

  Le DNS mini-buntu-admin sera maintenant utilisé en priorité pour toutes les résolutions.

  4. For WSL (current environment):

    sudo chattr -i /etc/resolv.conf
    sudo rm /etc/resolv.conf
    echo -e "nameserver 192.168.1.24\nsearch home.local" | sudo tee /etc/resolv.conf
    sudo bash -c 'echo "[network]" > /etc/wsl.conf'
    sudo bash -c 'echo "generateResolvConf = false" >> /etc/wsl.conf'
    sudo chattr +i /etc/resolv.conf
```



## 3. Install basic web server listening on 8080 on mini-buntu network card

*To be documented*

## 4. Setup DNS to make my-app:8080 targeting mini-buntu:8080

✅ **Completed** - This is handled by the nginx reverse proxy configuration above. The DNS entry `my-app.home.local` points to my-berry (192.168.1.24), and nginx on my-berry forwards all traffic to mini-buntu:8080.

## 5. Plan to be able to address http://my-app targeting mini-buntu:8080

✅ **Completed** - The reverse proxy setup allows accessing `http://my-app.home.local` (port 80) which automatically forwards to `http://mini-buntu:8080`. No need to specify port 8080 in the URL anymore.
