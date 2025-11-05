# 🧠 Guide complet sur la commande `bind` en Bash

## 📖 Introduction

La commande `bind` permet de **personnaliser les raccourcis clavier** utilisés dans Bash.  
Elle repose sur la bibliothèque **Readline**, utilisée par Bash pour la saisie interactive.

Grâce à `bind`, tu peux :
- Lister les raccourcis clavier existants  
- Créer des raccourcis pour exécuter des commandes Bash  
- Modifier ou supprimer des associations de touches  
- Rendre ces personnalisations persistantes dans `~/.inputrc`

---

## 🔍 1. Afficher les raccourcis clavier

### Lister toutes les liaisons actives
```bash
bind -p
```

### lister uniquement les touches :

```bash
bind -p
```

### Associer une touche à une commande Bash :

```bash
bind -x '"\C-l": clear'
```

> Quand tu appuies sur Ctrl+L, le terminal exécute la commande clear



### Autres fonctions utiles :

```bash
bind '"\C-a": beginning-of-line'   # Aller au début
bind '"\C-e": end-of-line'         # Aller à la fin
bind '"\C-k": kill-line'           # Supprimer jusqu’à la fin
bind '"\C-y": yank'                # Coller (yank)
```

### Récapitulatif des options utiles :

```bash
| Commande             | Description                                             |
| -------------------- | ------------------------------------------------------- |
| `bind -p`            | Liste toutes les liaisons Readline (fonctions internes) |
| `bind -P`            | Liste les fonctions Readline avec leur description      |
| `bind -x`            | Crée ou modifie une liaison vers une commande shell     |
| `bind -X`            | Liste les liaisons `bind -x` (commandes shell)          |
| `bind -r`            | Supprime une liaison                                    |
| `bind -f ~/.inputrc` | Charge un fichier de configuration Readline             |
```

