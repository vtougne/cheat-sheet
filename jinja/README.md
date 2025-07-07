


### Templating from string
```python
#!/usr/bin/env python3
from jinja2 import Environment, BaseLoader

myString = 'coucou {{ name  }}'
data = { "name": "vince "}
mplate = Environment(loader=BaseLoader()).from_string(myString)
data = mplate.render(**data)

print(data)

```

### add context

https://jinja.palletsprojects.com/en/3.0.x/api/#jinja2.Environment.add_extension


### compile expression
https://jinja.palletsprojects.com/en/3.0.x/api/#jinja2.Environment.add_extension

### globals
https://jinja.palletsprojects.com/en/3.0.x/api/#jinja2.Template.globals

