#!/usr/bin/python3
"""
Initialize a project directory to be used for a standalone python project.
"""
import argparse
import os
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument('scriptnames', type=str, nargs='+', help="Names for the Python scripts to be created.")
parser.add_argument('-d', '--directory', type=str, help="Directory to create the script(s) in. Defaults to CWD.", default='.')
parser.add_argument('-v', '--virtualenv', action='store_true', help="Create and activate a virtual environment for this project.")
args = parser.parse_args()

def initialize():
    #Create and/or navigate to directory based on -d argument.
    if os.path.isabs(args.directory):
        if not os.path.exists(args.directory):
            os.mkdir(args.directory)
        os.chdir(args.directory)
    elif args.directory != os.getcwd():
        if not os.path.exists(args.directory):
            os.mkdir(args.directory)
        os.chdir(args.directory)

    #Create any script files needed.
    for name in args.scriptnames:
        if os.path.splitext(name)[1] != '.py':
            name = os.path.splitext(name)[0] + '.py'
        create_file_command = 'touch {}'.format(name)
        subprocess.call(create_file_command, shell=True)
        newfile = open(name, 'w')
        newfile.write('#!/usr/bin/python3\n')
        newfile.close()

    if args.virtualenv:
        print('installing venv')
        subprocess.call('virtualenv venv -p python3', shell=True)

    print('Initialization completed')


if __name__ == '__main__':
    initialize()
