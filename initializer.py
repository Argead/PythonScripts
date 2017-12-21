#!/usr/bin/python3
"""
Initialize a project directory to be used for a standalone python project.
"""
import argparse
import os
import subprocess

parser = argparse.ArgumentParser()
#TODO: should be able to provide multiple names so multiple scripts are created.
parser.add_argument('scriptname', type=str, help="Name for the Python script.")
parser.add_argument('-d', '--directory', type=str, help="Directory to create the script(s) in. Defaults to CWD", default='.')
args = parser.parse_args()

def initialize():
    #TODO: Normalize the path provided by the argument, in case it does not match the path formatting used by the OS.
    #Create a directory if needed.
    current_dir = os.getcwd()
    if current_dir != os.path.abspath(args.directory):
        os.chdir(os.path.abspath(args.directory))

    #Create any script files needed.
    scriptname = args.scriptname
    if os.path.splitext(scriptname)[1] != '.py':
        scriptname = os.path.splitext(scriptname)[0] + '.py'
    create_file_command = 'touch {}'.format(scriptname)
    #TODO: Is shell=True always needed? Or is sys.platform conditional more useful?
    subprocess.call(create_file_command, shell=True)
    newfile = open(scriptname, 'w')
    newfile.write('#!/usr/bin/python3\n')
    newfile.close()

if __name__ == '__main__':
    initialize()
