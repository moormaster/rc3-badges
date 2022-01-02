#!/usr/bin/python3

import argparse
from jinja2 import Environment, DictLoader, select_autoescape
import json


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', type=str, required=True, dest='badges_file', help='JSON data file containing information about badges')
    parser.add_argument('-t', type=str, required=True, dest='template_file', help='Jinja2 html template to be rendered')
    parser.add_argument('-o', type=str, required=True, dest='output_file', help='Output html file to be written')

    return parser.parse_args()


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


def main(args):
    env = Environment(
        loader=DictLoader({'template': read_file(args.template_file)}),
        autoescape=select_autoescape()
    )
    
    template = env.get_template('template')
    badges = json.loads(read_file(args.badges_file))
    
    rendered_html = template.render(badges=badges)
    
    write_file(args.output_file, rendered_html)


if __name__ == '__main__':
    args = parse_arguments()
    main(args)
