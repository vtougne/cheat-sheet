#!/bin/bash

# Définir le nombre de lignes et de colonnes
ROWS=5
COLS=3

# Créer un tableau vide
declare -A tableau

# Remplir le tableau avec des données
for ((i=0; i<ROWS; i++))
do
  for ((j=0; j<COLS; j++))
  do
    tableau[$i,$j]=$((i * j))
  done
done

# Afficher le tableau
echo "Tableau de données:"
for ((i=0; i<ROWS; i++))
do
  for ((j=0; j<COLS; j++))
  do
    printf "%d " "${tableau[$i,$j]}"
  done
  echo ""
done
