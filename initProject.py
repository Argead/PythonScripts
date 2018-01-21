#!/usr/bin/python3

import os
import subprocess
import sys

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
            
def initialize_directory():
    init = subprocess.Popen(['git', 'init'], stdout=subprocess.PIPE)
    init.communicate()[0]
    print('Project init complete')
    
def add_origin(userName, projectName):
    repo_path = 'git@github.com:{}/{}.git'.format(userName, projectName)
    origin = subprocess.Popen(['git', 'remote', 'add', 'origin', ])
    remote_url = subprocess.Popen(['git', 'remote', 'set-url', 'origin', repo_path], stdout=subprocess.PIPE)
    remote_url_result = remote_url.communicate()[0]
    print('Origin added')
    
if __name__ == "__main__":
    import argpase
    parser = argparse.ArgumentParser()
    parser.add_argument('project', type=str)
    parser.add_argument('directory', default='.', type=str)
    parser.add_argument('userName', type=str)
    args = parser.parse_args()
    create_project_directory(args.project, args.directory)
    initialize_directory()
    add_origin(args.userName, args.project)
        