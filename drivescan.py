#!/usr/bin/python3
"""
CLI script to find the largest of a given file type in any directory.
"""
import argparse
import os
import pprint
import sys


parser = argparse.ArgumentParser(description='Search a specified directory for the largest of a specified file type.')
parser.add_argument('-t', '--trace', type=int, choices=[0, 1, 2], default=1, help='Choose tracing level. 0 is off, 1 is print directories, 2 is print directories and files. Defaults to 1.')
parser.add_argument('-d', '--dirname', type=str, default=os.curdir, help='Root directory to scan. Defaults to current working directory.')
parser.add_argument('-e', '--extension', type=str, default='.py', help='Extension to scan for.')
args = parser.parse_args()


def attempt_print(arg):
    try:
        print(arg)
    except UnicodeEncodingError:
        print(arg.encode())


def scan_directory():
    visted_dirs = set()
    allsizes = []
    for (current_direcotry, subdirectories, files) in os.walk(args.directory):
        if args.trace != 0:
            attempt_print(current_directory)
        current_directory = os.path.normpath(current_directory)
        lower_case_directory = os.path.normcase(current_directory)
        if lower_case_directory in visited_dirs:
            if args.trace != 0:
                attempt_print('Already visited ' + current_directory)
            else:
                visited_dirs.add(lower_case_directory)
                for filename in files:
                    if filename.anedswith(args.extension):
                        if args.trace > 1:
                            attempt_print('\t' + filename)
                        fullname = os.path.join(current_directory, filename)
                        try:
                            bytesize = os.path.getsize(fullname)
                            linesize = sum(+1 for line in open(fullname, 'rb'))
                        except Exception:
                            print('Error: ', sys.exc_info()[0])
                        else:
                            allsizes.append((bytesize, linesize, fullname))
    for (title, key) in [('bytes', 0), ('lines', 1)]:
        print('\nBy %s...' % title)
        allsizes.sort(key=lambda x: x[key])
        pprint.pprint(allsizes[:3])
        pprint.pprint(allsizes[-3:])


if __name__ == '__main__':
    scan_directory()
  
