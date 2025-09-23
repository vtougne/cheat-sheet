




# Topo
```
ssh vince@mini-buntu-admin
profil      type      nom interface IP            DNS name
admin-cnx   ethernet  eno1          192.168.1.34  mini-buntu-admin
app-cnx     ethernet  enp3s0        192.168.1.32  mini-buntu
```






# procédure
## 1 - Identifier adaptateur réseau

```bash
ethtool enp3s0 | grep -A10 'Supported link modes'
ethtool eno1 | grep -A10 'Supported link modes'
```

### Changer les noms des profiles de connexion

sudo nmcli connection modify 'Connexion filaire 1' connection.id 'admin-cnx'"
sudo nmcli connection modify netplan-enp3s0 connection.id 'app-cnx'




### scan networks names

```bash
nmap -sn 192.168.1.0/24 | grep "^Nmap scan" | sed "s/Nmap scan report for//g"
```

### Afficher les noms logiques des connexions

```
sudo nmcli connection show
NAME                 UUID                                  TYPE      DEVICE  
netplan-enp3s0       6effa1b1-280b-3785-9b52-c723b445fb3e  ethernet  enp3s0  
Connexion filaire 1  0bf19761-991f-3f27-a120-97c8c3ad6fdd  ethernet  eno1    
```


### modifier le snoms des interfaces réseau présentées sur le réseau
```bash

sudo nmcli connection show netplan-enp3s0 | grep name

ipv4.dhcp-hostname:                     ini-buntu-admin
```



### changer le hostname DHCP
```bash
sudo nmcli connection modify 'Connexion filaire 1' ipv4.dhcp-hostname 'mini-buntu'
sudo nmcli connection modify 'netplan-enp3s0' ipv4.dhcp-hostname 'mini-buntu'

sudo nmcli connection show "Connexion filaire 1" | grep ipv4.dhcp-hostname:
sudo nmcli connection show netplan-enp3s0 | grep ipv4.dhcp-hostname:

```


## Ansible

### get hostvars
```
ANSIBLE_LOAD_CALLBACK_PLUGINS=1 ANSIBLE_STDOUT_CALLBACK=json ansible -i inventory.yml all -m debug -a 'msg="{{ hostvars }}"'
ansible -i inventory.yml mini-buntu -m setup | jtable template "{{ (stdin | from_json).plays[0].tasks[0].hosts['mini-buntu'].ansible_facts | dict2items }}"
```


```
ANSIBLE_STDOUT_CALLBACK=json ansible -i mini-buntu.yml all -m setup
ansible -i inventory.yml mini-buntu -m setup | jtable -p "plays[0].tasks[0].hosts['mini-buntu'].ansible_facts.ansible_eno1" | less -S
```



## 2 - Installer DNS BIND9 (Berkeley Internet Name Domain)

```bash
sudo apt update && sudo apt install bind9 bind9utils bind9-doc
```

```

Voici comment utiliser BIND9 sur votre interface eno1 (192.168.1.34):

  Configuration de base

  1. Fichiers principaux:
  - /etc/bind/named.conf - Configuration principale
  - /etc/bind/named.conf.local - Zones locales
  - /etc/bind/named.conf.options - Options globales

● 2. Configuration pour écouter sur eno1:

  Éditer /etc/bind/named.conf.options:
  sudo nano /etc/bind/named.conf.options

  options {
      directory "/var/cache/bind";

      // Écouter sur eno1 (192.168.1.34)
      listen-on { 192.168.1.34; };
      listen-on-v6 { none; };

      // Autoriser les requêtes du réseau local
      allow-query { 192.168.1.0/24; localhost; };

      // Forwarders (DNS publics)
      forwarders {
          8.8.8.8;
          8.8.4.4;
      };

      dnssec-validation auto;
      auth-nxdomain no;
  };

● 3. Commandes de gestion:

  # Vérifier la configuration
  sudo named-checkconf

  # Démarrer/arrêter le service
  sudo systemctl start bind9
  sudo systemctl stop bind9
  sudo systemctl restart bind9

  # Activer au démarrage
  sudo systemctl enable bind9

  # Vérifier l'état
  sudo systemctl status bind9

  # Logs
  sudo journalctl -u bind9 -f

  4. Test du serveur DNS:
  # Tester depuis la machine locale
  nslookup google.com 192.168.1.34

  # Tester depuis une autre machine du réseau
  nslookup google.com 192.168.1.34

```


## 3 - Configurer le poste de travil pour accéder au nouveau serveur DNS
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

  # Configurer le DNS (remplacez "Ethernet" par le nom de votre interface)
  Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses "192.168.1.34","8.8.8.8"

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
  ```