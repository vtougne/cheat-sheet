#!/usr/bin/env python3

from jinja2 import Environment

context = {"name": "vince"}
env = Environment()



class Templater():
    def __init__(self, template_string):
        self.template_string = template_string
        self.template = env.from_string(template_string, globals=context)
    
    def render(self, vars):
        return self.template.render(vars)

template_strings = ["Hello {{ name }} {{ suffix }}", "Bonjour {{ name }} {{ suffix }}", "Hola {{ name }} {{ suffix }}"]

templates = []
for template_string in template_strings:
    templates  = templates +  [Templater(template_string)]

i=0
for template in templates:
    suffix = {"suffix": "How are you?"}
    print(templates[i].render(suffix))
    i+=1