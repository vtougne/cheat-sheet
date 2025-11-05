# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a network administration project for setting up port forwarding and DNS services on a raspberry.

- my-berry hosts the DNS
- mini-buntu hosts VM's


## Network Architecture

DNS:
- my-berry.home (192.168.1.24)

Lab:
- mini-buntu.home (192.168.1.32)                # exposing apps
- mini-buntu-admin.home (192.168.1.34)          # exposing ssh

mini-buntu system has two network interfaces:
- `eno1` (192.168.1.34) - admin-cnx connection for administrative access
- `enp3s0` (192.168.1.32) - app-cnx connection for application traffic

Both interfaces present as `mini-buntu-admin` and `mini-buntu` respectively on the network.


## Connexions with sudo access 
```
ssh vince@my-berry
ssh vince@mini-buntu-admin
```

## Goal
Wrting the procedure @lab_setup.md

## Plan 

- [x] Install / setup bind9 listening on my-berry
- [x] setup windows desktop to use mini-buntu-admin as main DNS
- [ ] install / setup nginx for port forwarding
- [x] Install basic web server listening on 8080 on mini-buntu network card
- [ ] setup DNS to make my-app:8080 targeting mini-buntu:8080
- [ ] plan to be able to adress http://my-app targeting mini-buntu:8080


