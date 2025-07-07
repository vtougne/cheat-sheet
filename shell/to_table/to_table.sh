#!/bin/bash

f_log() { local level="$1" ; shift ; printf "%s [%-10s] %s\n" "$(date +'%Y-%m-%d %H:%M:%S')" " $level" "$@" ;}

export IFS="
"
csv_input="$1"

if [[ -z "$csv_input" ]]; then
  echo "Usage: $0 <csv_file> [delimiter]"
  exit 1
fi
delimiter="${2:-,}"

if [[ ! -f "$csv_input" ]]; then
  echo "File not found: $csv_input"
  exit 1
fi

[ ! -z "$delimiter" ] && delimiter=","

declare -a fields=()
declare -a column_sizes=()

i=0
for field in $(head -n 1 "$csv_input" | tr "$delimiter" ' '); do
    fields+=("$field")
    rows_length=""
    declare -a column_data=()
    for row in $(cat "$csv_input" | cut -d "$delimiter" -f $((i + 1))); do
        rows_length="${rows_length}${#row}\n"
        column_data+=("$row")
    done
    column_size=$(echo -e "$rows_length" | sort -n | tail -1)
    column_sizes+=("$column_size")

    ((i++))
done



f_log debug "elements:\n${column_sizes[*]}"
f_log debug "elements indices: ${!column_sizes[@]}"
f_log debug "size: ${#column_sizes[@]}"

printf_cmd=""
for column_size in ${!column_sizes[@]} ; do
    # echo "Column size for index $column_size: ${column_sizes[$column_size]}"
    printf_cmd="$printf_cmd %-${column_sizes[$column_size]}s"
done
f_log debug "printf command:\n $printf_cmd"
# echo


for row in $(cat "$csv_input"); do
    echo "printf \"${printf_cmd:1}\n\"" "$row"
done


# echo "columns_data elements index: ${!columns_data[@]}"
f_log debug -e "elementscolumn_sizes :\n${column_data[1]}"
f_log debug "row count column_sizes: ${!column_data[@]}"
f_log debug "row count column_sizes: ${column_data[*]}"
f_log debug "${#column_data[@]}"
# for row_index in ${!columns_data[@]} ; do
#     echo "row_index: $row_index"

# done
row_count=${#column_data[@]}

# for ((row_index=0; row_index<row_count; row_index++)); do
#     # echo row_index: $row_index
#     for column_index in ${!column_sizes[@]}; do
#         echo "${columns_data[$column_index]}"
#     done
# done

echo
echo starting
echo "${columns_data[@]}"





