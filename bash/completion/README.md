

https://opensource.com/article/18/3/creating-bash-completion-script

https://www.gnu.org/software/bash/manual/html_node/A-Programmable-Completion-Example.html#A-Programmable-Completion-Example


```
complete -W "now tomorrow never" dothis
```


```
my_func() {
    printf "coucou bob"
}

complete -F my_func dothis
```
