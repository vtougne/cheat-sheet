#!/bin/bash

f_log() { local level="$1" ; shift ; printf "%s [%-10s] %s\n" "$(date +'%Y-%m-%d %H:%M:%S')" " $level" "$@" ;}

conf_base_name="$1"
if [[ -z "$conf_base_name" ]]; then
  echo "Usage: $0 <conf_base_name>"
  exit 1
fi

ls_cmd="ls -1 ${conf_base_name}*.cfg"
file_list=$(eval "$ls_cmd") || { f_log error "No configuration files found matching pattern ${conf_base_name}*.cfg"; exit 1; }


export IFS="
"

fields_str=$(echo "${file_list}" | sed 's/.*_\(.*\)\.cfg/\1/g')

declare -a fields=()
for field in ${fields_str} ; do
  fields+=("${field}")
done


keys_str=$(cat $file_list | grep -v '^#' | grep -v '^$' | cut -d'=' -f1 | sort -u)
declare -a keys=()
for key in ${keys_str} ; do
  keys+=("${key}")
done


random_string=$(tr -dc 'A-Za-z' < /dev/urandom | head -c 20)
separator=" ${random_string} "
separator="\" \""

declare -a records=()
declare -a values_length=()
declare -a record_values_length=()

attribute_name="key"
record="$attribute_name"
record_values_length+=(${#record})
for env in ${fields_str} ; do
  record+="${separator}${env}"
  record_values_length+=(${#env})
done
values_length+=("${record_values_length[*]}")
records+=("${record}")

for key_id in ${!keys[@]} ; do
    key=${keys[$key_id]}
    declare -a record_values_length=()
    # declare -a record=""
    record="${key}"
    record_values_length+=(${#key})
    for field_id in ${!fields[@]} ; do
      field_name=${fields[$field_id]}
      conf_file="${conf_base_name}${field_name}.cfg"
      value=$(cat "${conf_file}" | grep -m 1 "${key}" | cut -d"=" -f2 | sed "s/\"/${random_string}/g;s/[\$]/\\\\$/g")
      raw_value=$(cat "${conf_file}" | grep -m 1 "${key}" | cut -d"=" -f2 | sed "s/[\$]/\\\\$/g")
      record_values_length+=(${#raw_value})
      record+="${separator}${value}"
    done
    records+=("${record}")
    values_length+=("${record_values_length[*]}")
done

declare -a fields_with_attribute_name=("$attribute_name")
fields_with_attribute_name+=(${fields[@]})


declare -a max_length=()

for field_id in ${!fields_with_attribute_name[@]} ; do
    
    field_name=${fields_with_attribute_name[$field_id]}
    ((field_id_plus_1=field_id+=1))
    declare -a field_lengths=()
    for length in ${!values_length[@]} ; do
      field_lengths+=($(echo ${values_length[$length]} | cut -d" " -f $field_id_plus_1))
    done
    max_length_str=$(echo "${field_lengths[*]}" | sort -n | tail -1)
    max_length+=($max_length_str)
    printf_cmd+=" %-${max_length_str}s"
    
done



printf_cmd=${printf_cmd:1}

f_display_table() {
  
  for record_id in ${!records[@]} ; do
    eval "$(echo printf "\"$printf_cmd\"" \"${records[$record_id]}\")"
    echo
  done
}

f_display_table | sed "s/${random_string}/\"/g" 
