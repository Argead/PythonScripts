#!/usr/bin/python3
"""
Command line script to automate git commits/pushes to GH, using SSH connection.
"""
import os
import subprocess

def commit_and_push(filename, message='None', branch='master'):
    if type(message) == list:
        message = ' '.join(message)
    if filename in os.listdir():
        process1 = subprocess.Popen(['git', 'commit', filename, '-m', message], stdout=subprocess.PIPE)
        output1 = process1.communicate()[0]
        process2 = subprocess.Popen(['git', 'push', 'origin', branch], stdout=subprocess.PIPE)
        output2 = process2.communicate()[0]
        print('Commit & Push Completed')
    else:
        print('File not found in CWD')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='file you want to push')
    parser.add_argument('-m', '--message', nargs='+', default='No message', help='message to attach to the commit; defaults to "No message"')
    parser.add_argument('-b', '--branch', default='master', help='git branch to push to; defaults to master')
    args = parser.parse_args()
    commit_and_push(args.filename, args.message, args.branch)