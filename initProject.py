#!/usr/bin/python3

import argparse
import os
import subprocess
import sys


#first, create the needed directory in Projects
#second, initialize the project with git
#third, prompt the user to confirm if they want to connect to the project's remote repo; assumes that the remote repo already exists


def create_project_directory(project, directory='.'):
    if directory == '.':
        if os.path.exists(project):
            print('Directory already exists')
            return False
        else:
            os.mkdir(project)
            os.chdir(project)
            print('Directory setup complete')
    else:
        if sys.platform == 'linux':
            os.chdir('/')
            path_parts = directory.split(os.sep)
            for part in path_parts:
                if os.path.exists(part):
                    os.chdir(part)
                else:
                    os.mkdir(part)
                    os.chdir(part)
            print('Directory setup complete')
        elif sys.platform[:3] == 'win':
            path_parts = directory.split(os.pathsep)
            os.chdir(path_parts[0] + os.sep)
            path_parts = path_parts[1:]
            for part in path_parts:
                if os.path.exists(part):
                    os.chdir(part)
                else:
                    os.mkdir(part)
                    os.chdir(part)
            print('Directory setup complete')