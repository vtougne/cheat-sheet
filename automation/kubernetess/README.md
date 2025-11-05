


## Commandes essentielles de kubectl

```bash
kubectl cluster-info
kubectl get nodes
```

## Créer un Pod simple (à partir d’une image Docker) :
```bash
kubectl run my-first-pod --image=nginx --restart=Never
```

## lister les pods
```bash
kubectl get pods
NAME                              READY   STATUS    RESTARTS      AGE
hello-minikube-7d48979fd6-vscnz   1/1     Running   7 (18h ago)   2d22h
my-first-pod                      1/1     Running   0             26s
my-second-pod                     1/1     Running   0             2s
```