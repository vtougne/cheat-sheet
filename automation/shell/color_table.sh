#!/bin/bash


echo "******************************************************************************"
echo " Basic Colors with Effects "
echo "******************************************************************************"

for code in {30..37}; do
echo -en "\e[${code}m"'\\e['"$code"'m'"\e[0m"
echo -en "  \e[$code;1m"'\\e['"$code"';1m'"\e[0m"
echo -en "  \e[$code;3m"'\\e['"$code"';3m'"\e[0m"
echo -en "  \e[$code;4m"'\\e['"$code"';4m'"\e[0m"
echo -en "  \e[$((code+60))m"'\\e['"$((code+60))"'m'"\e[0m"
echo -en "  \e[2;5${effect};9;38;5;$((code-30))m\\\\e[2;5${effect};9;38;5;$((code-30))m${i}\x1b[0m"
echo -e "  \e[1;5${effect};9;38;5;$((code-30))m\\\\e[1;5${effect};9;38;5;$((code-30))m${i}\x1b[0m"
done


echo "******************************************************************************"
echo " Background 256 colors "
echo "******************************************************************************"

for i in {0..255}; do
    # Affiche le code couleur (avant-plan)
    printf "\033[48;5;%sm %3s \033[0m" "$i" "$i"
    # Retour à la ligne toutes les 16 couleurs
    if (( (i + 1) % 16 == 0 )); then
        echo
    fi
done


echo "******************************************************************************"
echo " Foreground 256 colors "
echo "******************************************************************************"


for i in {0..255}; do
    printf "\033[38;5;%sm%3s\033[0m " "$i" "$i"
    (( (i + 1) % 16 == 0 )) && echo
done






echo "******************************************************************************"
echo " RGB 24-bit Color Table "
echo "******************************************************************************"


for r in {0..255..51}; do
  for g in {0..255..51}; do
    for b in {0..255..51}; do
      printf "\033[48;2;%d;%d;%dm %02X%02X%02X \033[0m" "$r" "$g" "$b" "$r" "$g" "$b"
    done
    echo
  done
  echo
done
