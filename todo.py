#!/usr/bin/python3
"""
Utility that looks for instances of 'TODO' items in a target directory, and amasses them into a todo list.
"""
import argparse
import os
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', type=str, default='.', help="Directory that the search should start in.")
args = parser.parse_args()


def scan_for_todos():
    print('Generating To Do list...')
    os.chdir(os.path.realpath(args.directory))
    todofile = open('TODO.txt', 'w')
    for item in os.listdir():
        #os.path.isfile(item)
        if os.path.splitext(item)[1] == '.py' and os.path.splitext(item)[0] != 'todo':
            filepath = os.path.abspath(item)
            grep_command = 'grep TODO {}'.format(filepath)
            result = subprocess.run(grep_command, shell=True, stdout=subprocess.PIPE)
            if result.returncode == 0:
                todofile.write(filepath + '\n')
                todo_msgs = result.stdout.decode()
                for msg in todo_msgs.splitlines():
                    todofile.write(msg + '\n')
                todofile.write('\n')
    todofile.close()
    print('To Do list completed')


if __name__ == '__main__':
    scan_for_todos()
