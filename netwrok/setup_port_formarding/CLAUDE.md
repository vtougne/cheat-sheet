# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a network administration project for setting up port forwarding and DNS services using Ansible. The setup involves configuring a dual-interface server (mini-buntu) with DNS capabilities using BIND9.

## Network Architecture

The target system has two network interfaces:
- `eno1` (192.168.1.34) - admin-cnx connection for administrative access
- `enp3s0` (192.168.1.32) - app-cnx connection for application traffic

Both interfaces present as `mini-buntu-admin` and `mini-buntu` respectively on the network.

## Files and subject to ignore 
files:
- view_hostvars.yml
subjetcs:
- Ansible
- notes using my personal project jtable


## Target 

[x] - setup mini-buntu networks cards


## Key Commands

### Network Interface Management
```bash
# Check network adapter capabilities
ethtool enp3s0 | grep -A10 'Supported link modes'
ethtool eno1 | grep -A10 'Supported link modes'

# Modify NetworkManager connections
sudo nmcli connection modify 'Connexion filaire 1' connection.id 'admin-cnx'
sudo nmcli connection modify netplan-enp3s0 connection.id 'app-cnx'

# Set DHCP hostnames
sudo nmcli connection modify 'admin-cnx' ipv4.dhcp-hostname 'mini-buntu-admin'
sudo nmcli connection modify 'app-cnx' ipv4.dhcp-hostname 'mini-buntu'
```

### DNS/BIND9 Management
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
nslookup google.com 192.168.1.34
```

### Network Discovery
```bash
# Scan local network
nmap -sn 192.168.1.0/24 | grep "^Nmap scan" | sed "s/Nmap scan report for//g"
```

## Configuration Files

- `inventory.yml`: Ansible inventory defining the mini-buntu host with SSH configuration
- `view_hostvars.yml`: Ansible playbook for debugging host variables
- `notes.md`: Comprehensive documentation of network setup procedures and DNS configuration

## Important Network Details

The BIND9 DNS server is configured to:
- Listen on interface eno1 (192.168.1.34)
- Allow queries from 192.168.1.0/24 network
- Forward to public DNS (8.8.8.8, 8.8.4.4)
- Serve the local network with custom hostname resolution

The target host uses Python 3.12 at `/usr/bin/python3.12` for Ansible operations.

