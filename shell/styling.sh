#!/bin/bash




# for i in {0..255}; do
#     echo -e "\x1b[38;5;${i}mcolor${i}\x1b[0m"
# done



# for i in {0..32}; do
#     echo -e "\x1b[2;5;${i}mcolor${i}\x1b[0m"
# done


# echo -e "\x1b[2;5;9mcolor\x1b[0m"

# for i in {0..255}; do
#     echo -e "\x1b[2;2;9;38;2;${i}mcolor${i}\x1b[0m"
# done

for i in {0..255}; do
    for effect in 0 1 4 5 7 8 9; do
        echo -e "\x1b[2;5${effect};9;38;5;${i}mcolor${i}\x1b[0m"
    done
    # echo -e "\x1b[2;5;9;38;5;${i}mcolor${i}\x1b[0m"
done
