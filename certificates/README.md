


# connect external docker to gitlab registry

[certificate signed by unknown authority](https://docs.gitlab.com/ee/administration/packages/container_registry.html#using-self-signed-certificates-with-container-registry)

# show certificates

```bash
openssl s_client -showcerts -connect registry.msi-gitlab:443 </dev/null
```

# update certs
```bash
sudo update-ca-certificates --fresh
```
# export  cert on master

```bash
openssl s_client -showcerts -connect registry.msi-gitlab:443 -servername registry.msi-gitlab < /dev/null 2>/dev/null | openssl x509 -outform PEM > /tmp/registry.msi-gitlab.crt
```

# verify master cert

```bash
echo | openssl s_client -CAfile /tmp/registry.msi-gitlab.crt -connect registry.msi-gitlab:443 -servername registry.msi-gitlab:443
```



curl -vvv https://registry.msi-gitlab