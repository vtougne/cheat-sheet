#!/usr/bin/env python3

from jinja2 import Environment

context = {"name": "vince"}
env = Environment()


template_1 = env.from_string('Hello {{ name }} {{ answer }}',globals=context) 
template_2 = env.from_string('Good by {{ name }} {{ answer }}',globals=context) 
# template = env.from_string('Hello {{ name }} {{ answer }}') 

answer = "How are you doing today?"
out_str =  template_1.render({"answer": answer})
print(out_str)
out_str =  template_2.render({"answer": "see you soon"})
print(out_str)

