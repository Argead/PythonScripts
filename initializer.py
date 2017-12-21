#!/usr/bin/python3
"""
Initialize a project directory to be used for a standalone python project.
"""
import argparse
import os
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('scriptnames', type=str, nargs='+', help="Names for the Python scripts to be created.")
parser.add_argument('-d', '--directory', type=str, help="Directory to create the script(s) in. Defaults to CWD", default='.')
args = parser.parse_args()

def initialize():
    #Create a directory if needed.
    current_dir = os.getcwd()
    if current_dir != os.path.abspath(args.directory):
        os.chdir(os.path.abspath(os.path.normpath(args.directory)))

    #Create any script files needed.
    for name in args.scriptnames:
        if os.path.splitext(name)[1] != '.py':
            name = os.path.splitext(name)[0] + '.py'
        create_file_command = 'touch {}'.format(name)
        subprocess.call(create_file_command, shell=True)
        newfile = open(name, 'w')
        newfile.write('#!/usr/bin/python3\n')
        newfile.close()

if __name__ == '__main__':
    initialize()
