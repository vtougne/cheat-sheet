[[_TOC_]]

# 🧠 Guide complet sur la commande `trap` en Bash

### Nettoyage automatique avant de quitter :

```bash
#!/bin/bash
tmpfile=$(mktemp)

# Supprime le fichier temporaire à la fin, quelle que soit la sortie
trap 'rm -f "$tmpfile"' EXIT

echo "Travail en cours, fichier temporaire : $tmpfile"
sleep 2
echo "Fini !"
```

### Intercepter un Ctrl+C (SIGINT) :

```bash
#!/bin/bash
trap 'echo "Interruption détectée (Ctrl+C). Nettoyage..."; exit 1' SIGINT

echo "Appuie sur Ctrl+C pour tester..."
while true; do
    sleep 1
done
```


### Gérer plusieurs signaux :

```bash
#!/bin/bash
cleanup() {
  echo "Arrêt propre..."
  rm -f /tmp/my.lock
  exit
}

trap cleanup SIGINT SIGTERM EXIT
touch /tmp/my.lock
echo "Script en cours..."
sleep 60
```
> ➡️ Le cleanup s’exécute si le script reçoit SIGINT (Ctrl+C), SIGTERM (kill), ou lors de la fin (EXIT).

### Exécuter une commande avant chaque erreur (ERR) :

```bash
#!/bin/bash
set -e
trap 'echo "Une erreur est survenue à la ligne $LINENO"' ERR

echo "Tout va bien"
false  # Simule une erreur
echo "Cette ligne ne sera jamais exécutée"

```

### Exemple combiné :

```bash
#!/bin/bash
set -euo pipefail
tmpdir=$(mktemp -d)

cleanup() {
  echo "Nettoyage..."
  rm -rf "$tmpdir"
}
trap cleanup EXIT INT TERM

echo "Fichier temporaire : $tmpdir"
# Simule un traitement
sleep 2
echo "OK"
```



### Désactiver un trap :

```bash
trap - SIGINT
```



### ou tous les enlever :

```bash
trap - EXIT
```


