#!/usr/bin/python3
"""
CLI utility to find files matching a supplied filename pattern.
"""
import argparse
import fnmatch
import os
import sys


parser = argparse.ArgumentParser()
parser.add_argument('pattern', type=str, help='filename pattern to match to')
parser.add_argument('startdir', type=str, help='directory to start search in')
args = parser.parse_args()


def find(filename_pattern, start_directory=os.curdir):
    for (current_dir, subdirs, files) in os.walk(start_directory):
        for name in subdirs + files:
            if fnmatch.fnmatch(name, filename_pattern):
                full_file_path = os.path.join(current_dir, name)
                yield full_file_path

                
def find_list(filename_pattern, start_directory=os.curdir, sort=False):
    matches = list(find(pattern, start_directory))
    if sort:
        matches.sort()
    return matches

    
if __name__ == '__main__':
    for item in find(args.pattern, args.startdir):
        print(item)