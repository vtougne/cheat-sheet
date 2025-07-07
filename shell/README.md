### Liens

- [Les tableaux](http://www.ixany.org/fr/articles/introduction-aux-tableaux-en-bash/)


### Diff in memory

```bash
comm -31 <(echo -e "john\ndoe"| sort) <(echo -e "john\ndoe\nvince et des" | sort)     
```


### Completion
- sample script:

```bash
#!/bin/bash

# Fonction de complétion
_mycmd_completion() {
    local cur prev opts
    cur="${COMP_WORDS[COMP_CWORD]}"    # Mot en cours de complétion
    prev="${COMP_WORDS[COMP_CWORD-1]}" # Mot précédent

    opts="start stop resume"

    # Si c'est le premier argument, on propose les options
    if [[ ${COMP_CWORD} == 1 ]]; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    fi
}

# Enregistrer la fonction de complétion pour la commande `mycmd`
complete -F _mycmd_completion ./test_completion.sh
```

- list completions:  

```bash
complete -p 

```
- add completion:  

```bash
complete -F _mycmd_completion ./test_completion.sh
```

- completion path location:  

```bash
/usr/share/bash-completion/completions/
```

- install completion

```bash
install -m 644 my_completion /usr/share/bash-completion/completions/
```

