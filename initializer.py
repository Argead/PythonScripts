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
parser.add_argument('-f', '--flask', action='store_true', help="Install the flask framework. If the virtualenv option is selected, flask will be installed in the venv.")
parser.add_argument('-b', '--bottle', action='store_true', help="Install the bottle framework. If the virtualenv option is selected, bottle will be installed in the venv.")
parser.add_argument('-j', '--django', action='store_true', help="Install the django framework. If the virtualenv option is enabled, django will be installed in the venv.")
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

    #Setup a virtual environment for the project and install any required packages.
    if args.virtualenv:
        print('Installing venv...')
        subprocess.call('virtualenv venv -p python3', shell=True)
    #Optional setup for flask.
    if args.flask:
        print('Installing flask...')
        if args.virtualenv:
            pip3_path = os.getcwd() + '/ven/bin/pip3'
            install = 'install flask'
            flask_install_command = '{} {}'.format(pip3_path, install)
            subprocess.call(flask_install_command, shell=True)
        else:
            subprocess.call('pip3 install flask', shell=True)

    #Optional setup for bottle.
    if args.bottle:
        print('Installing bottle...')
        if args.virtualenv:
            pip3_path = os.getcwd() + '/venv/bin/pip3'
            install = 'install bottle'
            bottle_install_command = '{} {}'.format(pip3_path, install)
            subprocess.call(bottle_install_command, shell=True)
        else:
            subprocess.call('pip3 install bottle', shell=True)

    #Optional setup for django.
    if args.django:
        print('Installing django...')
        if args.virtualenv:
            pip3_path = os.getcwd() + '/venv/bin/pip3'
            install = 'install django'
            django_install_command = '{} {}'.format(pip3_path, install)
            subprocess.call(django_install_command, shell=True)
        else:
            subprocess.call('pip3 install django', shell=True)







    print('Initialization completed')


if __name__ == '__main__':
    initialize()
