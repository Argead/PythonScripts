#usr/bin/python3
"""
Initialize a bottle application to run a fast web experiment.
"""
import argparse
import os
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('directory', type=str, help="Name of directory to be created to contain the application.")
parser.add_argument('-v', '--virtualenv', action='store_true', help="Create a virtual environment for this project.")
args = parser.parse_args()

def initialize_directory():
    #Create and navigate to the dir from the directory argument.
    print('Setting up project directory...')
    if os.path.isabs(args.directory):
        if not os.path.exists(args.directory):
            #TODO: This mkdir call will likely fail for an abspath. More logic needed to handle creating the dir iteratively, esp. if more than one nested directory needs to be created.
            os.mkdir(args.directory)
    elif args.directory != os.getcwd():
        if not os.path.exists(args.directory):
            #TODO: This mkdir call will also fail if nested directories need to be created. Needs to split the args.directory provided and iterate over each dir level, validating whether it exists, creating it if not, then stepping into it and repeating the iteration.
            os.mkdir(args.directory)
    os.chdir(args.directory)
    
    #Create directory for static files.
    subprocess.call('mkdir static', shell=True)
    
    #Create the app.py file for the project.
    subprocess.call('touch app.py', shell=True)
    
    #Setup a virtualenv for the project if specified.
    if args.virtualenv:
        #TODO: validate that virtualenv is installed first.
        print('Installing virtual environment...')
        subprocess.call('virtualenv venv -p python3', shell=True)
        
    #Install bottle for the project.
    print('Installing bottle framework...')
    if args.virtualenv:
        #TODO: logic to confirm if pip3 is installed and to install it if not.
        pip3_path = os.getcwd() + '/venv/bin/pip3'
        install_cmd = 'install bottle'
        bottle_install_command = '{} {}'.format(pip3_path, install_cmd)
        subprocess.call(bottle_install_command, shell=True)
    else:
        subprocess.call('pip3 install bottle', shell=True)

    #Install bottle-sqlite module.
    print('Installing bottle-sqlite module...')
    if args.virtualenv:
        pip3_path = os.getcwd() + '/venv/bin/pip3'
        install_cmd = 'install bottle-sqlite'
        orm_install_command = '{} {}'.format(pip3_path, install_cmd)
        subprocess.call(orm_install_command, shell=True)
    else:
        subprocess.call('pip3 install bottle-sqlite', shell=True)
        
        
    #Write boilerplate content into app.py. This is temporary, until a better alternative is implemented.    
    app_file = open('app.py', 'w')
    app_file.write('#!/usr/bin/python3' + os.linesep * 2)
    app_file.write('import bottle' + os.linesep)
    app_file.write('import bottle-sqlite' + os.linesep)
    app_file.write('import sqlite3' + os.linesep)
    app_file.write(os.linesep * 2)
    app_file.write('app = bottle.Bottle()' + os.linesep)
    app_file.write('plugin = bottle.ext.sqlite.Plugin(dbfile=/test.db)' + os.linesep)
    app_file.write('app.install(plugin)' + os.linesep * 2)
    
    #Index Route logic
    app_file.write('@route("/", method="GET")' + os.linesep)
    app_file.write('def index():' + os.linesep)
    app_file.write('\treturn "index route"' + os.linesep)
    
    #App launch logic
    app_file.write(os.linesep * 2)
    app_file.write('run(host="localhost", port=8000, debug=False')
    app_file.close()


    print('Initialization completed')
    
if __name__ == '__main__':
    initialize_directory()
        
    
