f_var_loader() {
# This function loads environment variables from a configuration file.

    conf_file=$1
    [[ -z "${conf_file}" ]] && { echo "Usage: $0 <conf_file>"; return 1; }
    [[ ! -f "${conf_file}" ]] && { echo "Configuration file ${conf_file} does not exist."; return 1; }
    export OLD_IFS="${IFS}"
    export IFS='='
    while read -r key value; do
        if [[ -n "${key}" && -n "${value}" ]]; then
            export "${key}"="${value}"
        fi
    done <<<$(cat "${conf_file}")

    loader_env=$(echo ${conf_file} | sed 's/.*_\(.*\)\.cfg/\1/g')
    loader_app=${conf_file%_*}
    keys_str=$(cat "${conf_file}" | grep -v '^#' | grep -v '^$' | cut -d'=' -f1 | sort -u)

    var_file="${loader_app}_vars.sh"
    set -a
    if [[ -f "${var_file}" ]]; then

        evalued_keys_str=$(cat "${var_file}" | grep -v '^#' | grep -v '^$' | cut -d'=' -f1 | sort -u)
        . "${var_file}" 2>/dev/null || { echo "Error sourcing ${var_file}"; return 1; }

    fi

    # echo "debug password: ${password}"
    # echo "debug loader_env: ${loader_env}"
    # echo "debug loader_app: ${loader_app}"
    # echo -e "debug keys_str:\n${keys_str}\n"
    # echo -e "debug evaluated_keys_str:\n${evalued_keys_str}\n"


    # echo "debug env_letter: ${env_letter}"
    export IFS="${OLD_IFS}"

}