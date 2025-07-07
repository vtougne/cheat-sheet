#!/bin/bash

for code in {30..37}; do
echo -en "\e[${code}m"'\\e['"$code"'m'"\e[0m"
echo -en "  \e[$code;1m"'\\e['"$code"';1m'"\e[0m"
echo -en "  \e[$code;3m"'\\e['"$code"';3m'"\e[0m"
echo -en "  \e[$code;4m"'\\e['"$code"';4m'"\e[0m"
echo -en "  \e[$((code+60))m"'\\e['"$((code+60))"'m'"\e[0m"
echo -en "  \e[2;5${effect};9;38;5;$((code-30))m\\\\e[2;5${effect};9;38;5;$((code-30))m${i}\x1b[0m"
echo -e "  \e[1;5${effect};9;38;5;$((code-30))m\\\\e[1;5${effect};9;38;5;$((code-30))m${i}\x1b[0m"
done