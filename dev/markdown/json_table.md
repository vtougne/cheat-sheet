

## json table
```json:table
{
    "items" : [
      {"a": "11", "b": "22", "c": "33"}
    ]
}
```

## filtred table

```json:table
{
    "fields" : [
        {"key": "a", "label": "AA"},
        {"key": "b", "label": "BB"},
        {"key": "c", "label": "CC"}
    ],
    "items" : [
      {"a": "11", "b": "22", "c": "33"},
      {"a": "211", "b": "222", "c": "233"}
    ],
    "filter" : true
}
```


## filtred table markdon attributes

```json:table
{
    "fields" : [
        {"key": "a", "label": "AA"},
        {"key": "b", "label": "**BB**"},
        {"key": "c", "label": "CC"}
    ],
    "items" : [
      {"a": "11", "b": "$`\textcolor{red}{\text{coucou}}`$", "c": "33"},
      {"a": "#1", "b": "222", "c": "233"}
    ],
    "markdown" : true,
    "caption" : ""
}
```
    // "markdown" : true

## sorting elements

```json:table
{
    "fields" : [
        {"key": "a", "label": "AA", "sortable": true},
        {"key": "b", "label": "BB"},
        {"key": "c", "label": "CC"}
    ],
    "items" : [
      {"a": "11", "b": "22", "c": "33"},
      {"a": "211", "b": "222", "c": "233"}
    ]
}
```

## sorting elements + filter

```json:table
{
    "fields" : [
        {"key": "the truc", "sortable": true},
        {"key": "b", "label": "BB", "sortable": true},
        {"key": "c", "label": "CC", "sortable": true}
    ],
    "items" : [
      {"the truc": "11", "b": "22", "c": "33"},
      {"the truc": "211", "b": "222", "c": "233"}
    ],
    "filter": true
}
```





## simple

first name | last name | adress
--- | ---- | ---- 
john | ***doe*** | 15, truc of
William | pi | far far