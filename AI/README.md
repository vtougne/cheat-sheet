# Claude Code


### Permettre Claude code de connaitre les fichiers / lignes sélectionnées dans VS code

Rechercher l'emplacement de vscode, et se posistionner dans le répertoire de projet

```bash
/mnt/c/Users/vtoug/AppData/Local/Programs/Microsoft VS Code/bin/code' $(pwd)
```

### VS code setup

### mise à jour Claude Code
```bash
sudo npm i -g @anthropic-ai/claude-code
```


### Ne pas demander d'autorisation pour lancer des lignes de commandes

```bash
claude --dangerously-skip-permissions
```
