
```bash
watch -t 'docker ps --format "table {{.Names}}\t{{.State}}\t{{.Status}}"'
```



```bash
docker run --privileged --name my-dind-container -d docker:dind
```


