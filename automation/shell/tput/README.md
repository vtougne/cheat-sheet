[[_TOC_]]

# 🧠 Guide complet sur la commande `tput` en Bash

## 📖 Introduction

`tput` est une commande shell qui permet de contrôler l'affichage du terminal en utilisant la base de données **terminfo**. Elle sert à :
- Manipuler les couleurs du texte et de l'arrière-plan
- Déplacer le curseur à des positions précises
- Effacer des parties de l'écran
- Modifier le style du texte (gras, souligné, clignotant...)
- Récupérer des informations sur le terminal (dimensions, capacités)

---

## 📚 Syntaxe de base

```bash
tput [options] capname [paramètres]
```

**Options principales :**
- `-T type` : Spécifier le type de terminal (par défaut : $TERM)
- `-S` : Lire plusieurs commandes depuis stdin

---

## 🎨 Gestion des couleurs

### Couleurs du texte (foreground)

```bash
tput setaf <code_couleur>
```

### Couleurs de l'arrière-plan (background)

```bash
tput setab <code_couleur>
```

### Codes couleurs standard (0-7)

| Code | Couleur |
|------|---------|
| 0    | Noir    |
| 1    | Rouge   |
| 2    | Vert    |
| 3    | Jaune   |
| 4    | Bleu    |
| 5    | Magenta |
| 6    | Cyan    |
| 7    | Blanc   |

### Exemple de couleurs

```bash
# Texte en rouge
echo "$(tput setaf 1)Texte rouge$(tput sgr0)"

# Texte vert sur fond bleu
echo "$(tput setaf 2)$(tput setab 4)Texte vert sur fond bleu$(tput sgr0)"

# Réinitialiser les couleurs
tput sgr0
```

> Affiche du texte coloré et réinitialise le style à la normale

---

## 🖱️ Contrôle du curseur

### Positionnement du curseur

```bash
# Déplacer le curseur à la ligne Y, colonne X (commence à 0,0)
tput cup <ligne> <colonne>

# Exemple : positionner à la ligne 10, colonne 20
tput cup 10 20
echo "Texte à cette position"
```

### Déplacement relatif

```bash
tput cuu <n>  # Monter de n lignes (Cursor Up)
tput cud <n>  # Descendre de n lignes (Cursor Down)
tput cuf <n>  # Avancer de n colonnes (Cursor Forward)
tput cub <n>  # Reculer de n colonnes (Cursor Backward)
```

### Visibilité du curseur

```bash
tput civis    # Cacher le curseur (invisible)
tput cnorm    # Afficher le curseur (normal)
```

---

## 🧹 Effacement de l'écran

```bash
tput clear    # Effacer tout l'écran
tput el       # Effacer de la position du curseur jusqu'à la fin de la ligne
tput el1      # Effacer du début de la ligne jusqu'au curseur
tput ed       # Effacer de la position du curseur jusqu'à la fin de l'écran
```

---

## ✨ Styles de texte

```bash
tput bold     # Texte en gras
tput dim      # Texte atténué
tput smul     # Activer le soulignement (start underline)
tput rmul     # Désactiver le soulignement (remove underline)
tput rev      # Inverser les couleurs (reverse)
tput blink    # Texte clignotant
tput invis    # Texte invisible
tput smso     # Mode "standout" (souvent gras ou inversé)
tput rmso     # Fin du mode "standout"
tput sgr0     # Réinitialiser TOUS les attributs
```

### Exemple combiné

```bash
echo "$(tput bold)$(tput setaf 1)Texte rouge en gras$(tput sgr0)"
echo "$(tput smul)Texte souligné$(tput rmul)"
```

---

## 📏 Informations sur le terminal

```bash
tput cols     # Nombre de colonnes du terminal
tput lines    # Nombre de lignes du terminal

# Exemple d'utilisation
COLS=$(tput cols)
LINES=$(tput lines)
echo "Terminal : ${COLS}x${LINES}"
```

---

## 💡 Exemples pratiques

### Créer un menu coloré

```bash
#!/bin/bash

# Fonction pour afficher le menu
show_menu() {
    tput clear
    tput cup 2 10
    echo "$(tput bold)$(tput setaf 4)=== MENU PRINCIPAL ===$(tput sgr0)"
    tput cup 4 10
    echo "$(tput setaf 2)1.$(tput sgr0) Option 1"
    tput cup 5 10
    echo "$(tput setaf 2)2.$(tput sgr0) Option 2"
    tput cup 6 10
    echo "$(tput setaf 2)3.$(tput sgr0) Quitter"
    tput cup 8 10
    echo -n "$(tput bold)Votre choix : $(tput sgr0)"
}

show_menu
```

> Affiche un menu centré avec des couleurs

### Barre de progression

```bash
#!/bin/bash

progress_bar() {
    local duration=${1}
    local cols=$(tput cols)
    local bar_width=$((cols - 20))

    tput civis  # Cacher le curseur

    for ((i=0; i<=100; i++)); do
        local filled=$((bar_width * i / 100))
        local empty=$((bar_width - filled))

        tput cup 10 5
        printf "Progression: ["
        printf "%${filled}s" | tr ' ' '='
        printf "%${empty}s" | tr ' ' ' '
        printf "] %3d%%" $i

        sleep ${duration}
    done

    tput cnorm  # Réafficher le curseur
    echo
}

progress_bar 0.05
```

> Crée une barre de progression animée

### Message d'erreur stylisé

```bash
#!/bin/bash

error() {
    echo "$(tput bold)$(tput setaf 1)[ERREUR]$(tput sgr0) $1" >&2
}

success() {
    echo "$(tput bold)$(tput setaf 2)[OK]$(tput sgr0) $1"
}

warning() {
    echo "$(tput bold)$(tput setaf 3)[ATTENTION]$(tput sgr0) $1"
}

# Utilisation
error "Fichier introuvable"
success "Opération réussie"
warning "Espace disque faible"
```

> Affiche des messages avec des codes couleurs selon le type

### Centrer du texte

```bash
#!/bin/bash

center_text() {
    local text="$1"
    local cols=$(tput cols)
    local text_length=${#text}
    local padding=$(( (cols - text_length) / 2 ))

    printf "%${padding}s%s\n" "" "$text"
}

tput clear
center_text "$(tput bold)Texte centré$(tput sgr0)"
```

> Centre un texte horizontalement dans le terminal

---

## 🔧 Cas d'usage avancés

### Animation de chargement

```bash
#!/bin/bash

spinner() {
    local pid=$1
    local delay=0.1
    local spinstr='|/-\'

    tput civis
    while kill -0 $pid 2>/dev/null; do
        local temp=${spinstr#?}
        printf " [%c]  " "$spinstr"
        spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    tput cnorm
    printf "    \b\b\b\b"
}

# Utilisation
sleep 5 &
spinner $!
echo "$(tput setaf 2)Terminé!$(tput sgr0)"
```

### Tableau formaté

```bash
#!/bin/bash

# Dessiner un tableau
draw_table() {
    tput clear
    local width=50
    local height=10

    # En-tête
    tput cup 2 5
    echo "$(tput bold)$(tput setaf 4)╔$(printf '═%.0s' {1..48})╗$(tput sgr0)"

    tput cup 3 5
    echo "$(tput bold)$(tput setaf 4)║$(tput sgr0) $(tput bold)TABLEAU DE DONNÉES$(tput sgr0)                          $(tput bold)$(tput setaf 4)║$(tput sgr0)"

    tput cup 4 5
    echo "$(tput bold)$(tput setaf 4)╠$(printf '═%.0s' {1..48})╣$(tput sgr0)"

    # Lignes de données
    local line=5
    for i in {1..5}; do
        tput cup $line 5
        echo "$(tput setaf 4)║$(tput sgr0) Ligne $i                                     $(tput setaf 4)║$(tput sgr0)"
        ((line++))
    done

    # Bas du tableau
    tput cup $line 5
    echo "$(tput bold)$(tput setaf 4)╚$(printf '═%.0s' {1..48})╝$(tput sgr0)"
}

draw_table
```

### Écran interactif avec zones fixes

```bash
#!/bin/bash

init_screen() {
    tput clear
    tput civis

    # En-tête fixe
    tput cup 0 0
    tput setab 4
    tput setaf 7
    printf "%*s" $(tput cols) ""
    tput cup 0 2
    echo "$(tput bold)Application Shell - v1.0$(tput sgr0)"

    # Pied de page fixe
    local last_line=$(($(tput lines) - 1))
    tput cup $last_line 0
    tput setab 4
    tput setaf 7
    printf "%*s" $(tput cols) ""
    tput cup $last_line 2
    echo "$(tput bold)F1: Aide | F10: Quitter$(tput sgr0)"

    # Zone de contenu
    tput sgr0
    tput cup 2 0
}

cleanup() {
    tput clear
    tput cnorm
    tput sgr0
}

trap cleanup EXIT

init_screen
tput cup 3 2
echo "Contenu de l'application..."
sleep 3
```

---

## 📋 Référence rapide des capacités

| Capacité | Description |
|----------|-------------|
| `cols` | Nombre de colonnes |
| `lines` | Nombre de lignes |
| `clear` | Effacer l'écran |
| `cup Y X` | Positionner le curseur |
| `setaf N` | Couleur avant-plan |
| `setab N` | Couleur arrière-plan |
| `bold` | Texte en gras |
| `sgr0` | Réinitialiser les attributs |
| `civis` | Cacher le curseur |
| `cnorm` | Afficher le curseur |
| `el` | Effacer la ligne |
| `smul` | Activer soulignement |
| `rmul` | Désactiver soulignement |

---

## ⚠️ Bonnes pratiques

1. **Toujours réinitialiser les styles** : Utilisez `tput sgr0` après avoir modifié le style
2. **Gérer les erreurs** : Vérifiez que `tput` est disponible avec `command -v tput`
3. **Restaurer le curseur** : Utilisez `trap` pour garantir que le curseur est réaffiché en cas d'erreur
4. **Compatibilité** : Testez sur différents terminaux car toutes les capacités ne sont pas supportées partout
5. **Variables** : Stockez les séquences dans des variables pour éviter les répétitions

```bash
# Exemple de bonnes pratiques
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
BOLD=$(tput bold)
RESET=$(tput sgr0)

cleanup() {
    tput cnorm
    tput sgr0
}

trap cleanup EXIT

echo "${BOLD}${GREEN}Message important${RESET}"
```
## Table des couleurs

```bash
for i in {0..255}; do echo "$(tput setaf $i)Hello ${i}${RESET}"; done

for i in {0..255}; do echo "$(tput bold)$(tput setaf $i)Hello ${i}$(tput sgr0)"; done
```
---

## 🔗 Ressources complémentaires

- Page man : `man tput`
- Base de données terminfo : `man terminfo`
- Liste des capacités : `infocmp`
- Tester une capacité : `tput -S <<< "capname"`

---

**Note** : Certaines capacités peuvent varier selon le type de terminal ($TERM). Utilisez `echo $TERM` pour connaître votre type de terminal actuel.




## Table des couleurs

```bash
for i in {0..255}; do echo "$(tput setaf $i)Hello ${i}${RESET}"; done

for i in {0..255}; do echo "$(tput bold)$(tput setaf $i)Hello ${i}$(tput sgr0)"; done
```


# Cas d'usage



## lire et restaurer le contenu du terminal via tput smcup / tput rmcup



```bash
tput smcup   # active un écran secondaire
echo "Interface temporaire"
sleep 2
tput rmcup   # restaure l’écran précédent
```
