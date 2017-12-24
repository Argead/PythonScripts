#!/usr/bin/python3
"""
Command Line utility to show a python module's help and documentation text without starting an interactive Python session.
"""
import argparse
import os
import pprint

parser = argparse.ArgumentParser()
parser.add_argument('modules', type=str, nargs='+', help="List the arguments you want to read help and documentation text for.")
args = parser.parse_args()


def iterate_over_modules(modules):
    for module in modules:
        get_help_text(module)


def get_help_text(module='None'):
    print('Getting help text for {}...'.format(module))
    print(os.linesep * 2)
    module_to_import = __import__(module)
    pprint.pprint(help(module_to_import))
    print('Getting documentation for {}...'.format(module))
    pprint.pprint(module_to_import.__doc__)
    print(os.linesep * 4)



if __name__ == '__main__':
    iterate_over_modules(args.modules)



