#!/usr/bin/env python3

from jinja2 import Environment

env = Environment()
expr = env.compile_expression('(foo + 1) | string + "bar"')
print(expr(foo=23))






