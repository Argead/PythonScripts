#!/usr/bin/python3
"""
Command Line Utility that replaces all horizontal tabs with 4 spaces in a given Python file.
"""
import argparse
import os
import re

parser = argparse.ArgumentParser(description='Replace tabs with spaces in a Python file.')
parser.add_argument('filename', type=str, help='The Python script you want to replace horizontal tabs in.')
parser.add_argument('-v', '--verbose', action='store_true', help='Run script with higher verbosity.')
args = parser.parse_args()


#Initially, you provide the name of a file as the only argument. Later this can be enhanced, to either pass a directory (in which case the script scans every file in the directory), or a single Python file as before.


def replace_tabs():
    tab_pattern = '\t'
    spaces = '    '
    if args.filename.endswith('py'):
        if args.verbose:
            print('Replacing tabs in: {}'.format(args.filename))
        with open(args.filename, 'r') as source_file, open('dest_file.py', 'w') as dest_file:
            for line in source_file:
                edited_line = re.sub(tab_pattern, spaces, line)
                dest_file.write(edited_line)
    os.remove(args.filename)
    os.rename('dest_file.py', args.filename)
    
    

if __name__ == '__main__':
    replace_tabs()
