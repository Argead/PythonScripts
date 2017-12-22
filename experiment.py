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
    if ospath.isabs(args.directory):
        if not os.path.exists(args.directory):
            #TODO: This mkdir call will likely fail for an abspath. More logic needed to handle creating the dir iteratively, esp. if more than one nested directory needs to be created.
            os.mkdir(args.directory)
    elif args.directory != os.getcwd():
        if not os.path.exists(args.directory):
            #TODO: This mkdir call will also fail if nested directories need to be created. Needs to split the args.directory provided and iterate over each dir level, validating whether it exists, creating it if not, then stepping into it and repeating the iteration.
            os.mkdir(args.directory)
    os.chdir(args.directory)
    
    #Create the app.py file for the project.
    subprocess.call('touch app.py', shell=True)
    
    #Setup a virtualenv for the project if specified.
    if args.virtualenv:
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
        
    print('Initialization completed')
    
if __name__ == '__main__':
    initialize_directory()
        
    