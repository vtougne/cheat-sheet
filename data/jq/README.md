

### list keys

```
<daset>  | jq "keys"
<daset> | jq -r '.["something"] | .something_else | keys'
```




### list keys_unsorted

```
<dataset>  | jq -r '.[].something|keys_unsorted[]'
```
