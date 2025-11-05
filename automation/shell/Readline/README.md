[[_TOC_]]

# 🧠 Guide complet sur les commandes Readline en Bash

## 📖 Introduction

Readline est une bibliothèque GNU qui gère l'édition de ligne de commande dans les shells Unix (Bash, Zsh, etc.). Elle permet de naviguer, éditer et rechercher dans l'historique des commandes de manière efficace grâce à de nombreux raccourcis clavier.

Ce guide présente les raccourcis les plus utiles pour améliorer votre productivité dans le terminal.

---

## 🔍 1. Déplacement du curseur

### Déplacement par caractère
| Raccourci | Description |
|-----------|-------------|
| `Ctrl + F` | Avancer d'un caractère (Forward) |
| `Ctrl + B` | Reculer d'un caractère (Backward) |
| `→` | Avancer d'un caractère |
| `←` | Reculer d'un caractère |

### Déplacement par mot
| Raccourci | Description |
|-----------|-------------|
| `Alt + F` | Avancer d'un mot |
| `Alt + B` | Reculer d'un mot |
| `Ctrl + →` | Avancer d'un mot (alternative) |
| `Ctrl + ←` | Reculer d'un mot (alternative) |

### Déplacement en début/fin de ligne
| Raccourci | Description |
|-----------|-------------|
| `Ctrl + A` | Aller au début de la ligne |
| `Ctrl + E` | Aller à la fin de la ligne |
| `Home` | Aller au début de la ligne |
| `End` | Aller à la fin de la ligne |

---

## ✂️ 2. Édition et suppression

### Suppression de caractères
| Raccourci | Description |
|-----------|-------------|
| `Ctrl + D` | Supprimer le caractère sous le curseur (Delete) |
| `Backspace` | Supprimer le caractère avant le curseur |
| `Ctrl + H` | Supprimer le caractère avant le curseur |

### Suppression de mots et portions de ligne
| Raccourci | Description |
|-----------|-------------|
| `Alt + D` | Supprimer du curseur jusqu'à la fin du mot |
| `Alt + Backspace` | Supprimer du curseur jusqu'au début du mot |
| `Ctrl + W` | Supprimer le mot avant le curseur |
| `Ctrl + K` | Supprimer du curseur jusqu'à la fin de la ligne (Kill) |
| `Ctrl + U` | Supprimer du curseur jusqu'au début de la ligne |
| `Ctrl + X Backspace` | Supprimer du début de la ligne jusqu'au curseur |

### Copier/Coller (Kill ring)
| Raccourci | Description |
|-----------|-------------|
| `Ctrl + Y` | Coller le dernier texte supprimé (Yank) |
| `Alt + Y` | Faire défiler les éléments du kill ring (après Ctrl+Y) |

### Autres opérations d'édition
| Raccourci | Description |
|-----------|-------------|
| `Ctrl + T` | Échanger les deux derniers caractères (Transpose) |
| `Alt + T` | Échanger les deux derniers mots |
| `Alt + U` | Mettre en majuscule du curseur à la fin du mot |
| `Alt + L` | Mettre en minuscule du curseur à la fin du mot |
| `Alt + C` | Capitaliser le mot (première lettre en majuscule) |
| `Ctrl + _` | Annuler la dernière action (Undo) |
| `Alt + R` | Annuler toutes les modifications de la ligne courante |

---

## 📜 3. Historique des commandes

### Navigation dans l'historique
| Raccourci | Description |
|-----------|-------------|
| `↑` | Commande précédente dans l'historique |
| `↓` | Commande suivante dans l'historique |
| `Ctrl + P` | Commande précédente (Previous) |
| `Ctrl + N` | Commande suivante (Next) |
| `Alt + <` | Aller à la première commande de l'historique |
| `Alt + >` | Aller à la dernière commande de l'historique |

### Recherche dans l'historique
| Raccourci | Description |
|-----------|-------------|
| `Ctrl + R` | Recherche inversée dans l'historique (Reverse search) |
| `Ctrl + S` | Recherche avant dans l'historique (nécessite `stty -ixon`) |
| `Ctrl + G` | Quitter la recherche dans l'historique |
| `Ctrl + J` | Copier la commande trouvée sans l'exécuter |
| `Alt + P` | Recherche non-incrémentale en arrière |
| `Alt + N` | Recherche non-incrémentale en avant |

### Réutilisation de commandes
| Raccourci | Description |
|-----------|-------------|
| `!!` | Répéter la dernière commande |
| `!n` | Exécuter la commande numéro n de l'historique |
| `!-n` | Exécuter la commande n positions en arrière |
| `!string` | Exécuter la dernière commande commençant par "string" |
| `!?string` | Exécuter la dernière commande contenant "string" |
| `^old^new` | Répéter la dernière commande en remplaçant "old" par "new" |

---

## 🔄 4. Complétion et expansion

### Complétion
| Raccourci | Description |
|-----------|-------------|
| `Tab` | Compléter le nom de fichier/commande/variable |
| `Tab Tab` | Afficher toutes les complétions possibles |
| `Alt + ?` | Afficher les complétions possibles |
| `Alt + *` | Insérer toutes les complétions possibles |
| `Alt + /` | Compléter le nom de fichier |
| `Ctrl + X /` | Lister les complétions de chemin |
| `Alt + ~` | Compléter le nom d'utilisateur |
| `Alt + $` | Compléter le nom de variable |
| `Alt + @` | Compléter le nom d'hôte |
| `Alt + !` | Compléter le nom de commande |

### Expansion
| Raccourci | Description |
|-----------|-------------|
| `Alt + Ctrl + E` | Expansion de la ligne (variables, historique, etc.) |
| `Ctrl + X *` | Expansion de glob |
| `Ctrl + X $` | Expansion de variables |

---

## 🎮 5. Contrôle et macros

### Contrôle de l'exécution
| Raccourci | Description |
|-----------|-------------|
| `Ctrl + C` | Interrompre la commande en cours |
| `Ctrl + Z` | Suspendre la commande en cours (bg/fg pour reprendre) |
| `Ctrl + D` | Fermer le terminal (EOF) si ligne vide |
| `Ctrl + L` | Effacer l'écran (équivalent de `clear`) |
| `Ctrl + S` | Suspendre l'affichage (freeze) |
| `Ctrl + Q` | Reprendre l'affichage |

### Macros et répétitions
| Raccourci | Description |
|-----------|-------------|
| `Ctrl + X (` | Commencer l'enregistrement d'une macro |
| `Ctrl + X )` | Terminer l'enregistrement d'une macro |
| `Ctrl + X E` | Exécuter la dernière macro enregistrée |
| `Alt + [nombre]` | Répéter la prochaine commande n fois |

---

## ⚙️ 6. Configuration avec `.inputrc`

Le fichier `~/.inputrc` permet de personnaliser le comportement de Readline. Voici quelques configurations utiles :

```bash
# Créer ou éditer le fichier ~/.inputrc

# Ignorer la casse lors de la complétion
set completion-ignore-case on

# Complétion avec un seul Tab même s'il y a plusieurs possibilités
set show-all-if-ambiguous on

# Montrer immédiatement les complétions sans double Tab
set show-all-if-unmodified on

# Colorer les complétions selon le type de fichier
set colored-stats on

# Colorer les complétions comme avec ls --color
set colored-completion-prefix on

# Marquer les répertoires avec un /
set mark-directories on
set mark-symlinked-directories on

# Navigation dans l'historique avec les flèches selon le préfixe
"\e[A": history-search-backward
"\e[B": history-search-forward

# Mode vi (optionnel, à la place du mode emacs par défaut)
# set editing-mode vi

# Paginer les complétions si > 200 éléments
set page-completions on
set completion-query-items 200

# Bip visuel au lieu du bip sonore
set bell-style visible
```

Après modification du fichier, rechargez la configuration :
```bash
bind -f ~/.inputrc
```

---

## 🎯 7. Exemples pratiques

### Scénario 1 : Corriger une erreur dans une longue commande
```bash
# Vous avez tapé :
docker run -d --name mycontainer --port 8080:80 nginx

# Vous remarquez l'erreur "--port" au lieu de "-p"
# Solution :
1. Ctrl + A (aller au début)
2. Alt + F (x4 pour aller à --port)
3. Alt + D (supprimer --port)
4. Taper "-p"
```

### Scénario 2 : Rechercher et réexécuter une commande
```bash
# Vous voulez retrouver une commande git commit exécutée il y a longtemps
1. Ctrl + R
2. Taper "git commit"
3. Ctrl + R plusieurs fois pour naviguer dans les résultats
4. Entrée pour exécuter ou Ctrl + J pour éditer avant exécution
```

### Scénario 3 : Éditer une commande complexe
```bash
# Commande longue à éditer
1. Ctrl + A puis Ctrl + K pour tout supprimer
2. Ctrl + Y pour coller et recommencer
# Ou
1. Ctrl + X Ctrl + E pour ouvrir dans $EDITOR (vim/nano)
```

### Scénario 4 : Réutiliser des arguments
```bash
# Dernière commande
ls -la /var/log/nginx/access.log

# Nouvelle commande avec le dernier argument
cat !$
# Équivalent à : cat /var/log/nginx/access.log

# Ou avec Alt + . (point)
tail -f [Alt + .]
# Insère automatiquement /var/log/nginx/access.log
```

---

## 📚 8. Commandes utiles

### Afficher les raccourcis actifs
```bash
# Lister tous les raccourcis Readline
bind -P

# Lister les raccourcis avec leur fonction
bind -p

# Afficher les raccourcis par catégorie
bind -l
```

### Déboguer Readline
```bash
# Afficher les séquences de touches
cat -v
# Puis appuyer sur les touches pour voir leur séquence

# Tester une configuration
bash --rcfile ~/.inputrc
```

### Désactiver certains raccourcis
```bash
# Dans ~/.inputrc
"\C-s": ""  # Désactiver Ctrl+S
```

---

## 🔗 9. Ressources complémentaires

- [Documentation officielle GNU Readline](https://tiswww.case.edu/php/chet/readline/rltop.html)
- `man readline` - Manuel de Readline
- `man bash` - Section READLINE
- `info bash` - Documentation complète de Bash
- [Bash Reference Manual - Command Line Editing](https://www.gnu.org/software/bash/manual/html_node/Command-Line-Editing.html)

---

## 💡 Astuces finales

1. **Pratiquez régulièrement** : Les raccourcis deviennent naturels avec la pratique
2. **Commencez par les basiques** : `Ctrl+A`, `Ctrl+E`, `Ctrl+R`, `Ctrl+K`, `Ctrl+Y`
3. **Personnalisez votre `.inputrc`** : Adaptez Readline à votre workflow
4. **Activez la recherche incrémentale** : `Ctrl+R` est l'un des raccourcis les plus puissants
5. **Explorez le mode vi** : Si vous êtes un utilisateur vim, `set editing-mode vi` peut être intéressant

---

**Bon shell scripting !** 🚀
