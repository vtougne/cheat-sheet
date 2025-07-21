#!/bin/bash

f_log() { local level="$1" ; shift ; printf "%s [%-10s] %s\n" "$(date +'%Y-%m-%d %H:%M:%S')" " $level" "$@" ;}

config_base_name="$1"

cfg_ls_cmd="ls -1 ${config_base_name}*.cfg | tr '\n' ' '"
cfg_file_list="$(eval "$cfg_ls_cmd")" || { f_log error "No configuration files found matching pattern ${conf_base_name}*.cfg"; exit 1; }


# f_log debug "Found configuration files: ${cfg_file_list}"
var_file=

[ -f ${config_base_name}_vars.sh ] && var_file="${config_base_name}_vars.sh" 

# echo debug "Using variable file: ${var_file}"

all_key_cmd="cat  ${cfg_file_list} ${var_file} | grep -v '^#' | grep -v '^$' | cut -d'=' -f1 | sort -u"
all_keys="$(eval "$all_key_cmd")"

# echo -e debug "all_key_cmd:\n$all_key_cmd"
# echo -e debug "all_keys:\n$all_keys"
. var_loader.sh

work_path=/tmp/${config_base_name}

rm -rf "${work_path}"
mkdir -p "${work_path}" || { f_log error "Failed to create work directory ${work_path}"; exit 1; }


for file in ${cfg_file_list}; do
  unset $all_keys
  f_var_loader "${file}" || { f_log error "Failed to load variables from ${file}"; exit 1; }
  all_keys="$(echo -e "${keys_str}\n${evalued_keys_str}\n" | sort -u)"
#   echo -e debug "Loaded keys:\n${all_keys}"
  for key in ${all_keys}; do
    eval "key_value=\${${key}}"
    # echo "Processing key: ${key}: ${key_value}"
    echo "${key}=${key_value}" >> "${work_path}/${file}"
  done
done

# echo "./cfg2table.sh "${work_path}/${config_base_name}_""
# ./cfg2table.sh "${work_path}/${config_base_name}_"

./cfg2table.py -i "${work_path}/${config_base_name}"