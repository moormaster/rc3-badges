#!/usr/bin/python3

from jinja2 import Environment, DictLoader, select_autoescape
import json

def read_file(path):
    contents = None

    with open(path, mode='r', encoding='utf-8') as f:
        contents = f.read()
        f.close()

    return contents

def write_file(path, content):
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(content)
        f.close()

env = Environment(
    loader=DictLoader({'template': read_file('template.html.j2')}),
    autoescape=select_autoescape()
)

template = env.get_template('template')
badges = json.loads(read_file('badges.json'))

rendered_html = template.render(badges=badges)

write_file('badges.html', rendered_html)
