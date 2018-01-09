#!/usr/bin/env python3
"""
Simplified version of grep utility written in Python.
"""
import argparse
import os
import re
import sys


def grep(pattern, file, directories='recurse', quiet=False):
    matches = []
    try:
        re_pattern = re.compile(pattern)
    except re.error:
        if not quiet:
            sys.stderr.write('Error - invalid regex pattern: ')
            sys.stderr.write('{}\n'.format(sys.exc_info()[1]))
        return matches
    try:
        if not os.path.exists(file):
            if not quiet:
                sys.stdout.write('Error: file does not exist\n')
            return matches
        if os.path.isfile(file):
            with open(file, 'r') as target:
                for line in target.readlines():
                    if re_pattern.search(line):
                        matches.append(line)
        elif os.path.isdir(file):
            if directories == 'recurse':
                for (directory, subdirectories, dirFiles) in os.walk(file):
                    for dirFile in dirFiles:
                        with open(dirFile, 'r') as t:
                            for line in t.readlines():
                                if re_pattern.serach(line):
                                    match = (dirFile, line)
                                    matches.append(match)
            elif directories == 'read':
                dirPath = os.path.abspath(file)
                if re_pattern.search(dirPath):
                    matches.append(dirPath)
            elif directories == 'skip':
                pass
    except re.error as e:
        if not quiet:
            sys.stderr.write(e)
            sys.stderr.write('{}\n'.format(sys.exc_info()[1]))
    return matches


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern', type=str, help='regex pattern to match')
    parser.add_argument('file', type=str, help='file to search')
    
    parser.add_argument('-d', '--directories', choices=['recurse', 'read', 'skip'], default='recurse', type=str, help='Choose whether to recursively apply grep to a directory, read the directory name, or skip the directory')
    parser.add_argument('-q', '--quiet', action='store_true', help='suppress normal print output of grep')
    
    args = parser.parse_args()
    result = grep(args.pattern, args.file, args.directories, args.quiet)
    
    if len(result) > 0:
        for item in result:
            if type(item) != tuple:
                file_str = '\033[1;35;40m {} '.format(args.file)
                item_str = '\033[1;37;40m {}'.format(item)
                if not args.quiet:
                    sys.stdout.write('{}\t{}'.format(file_str, item_str))
            else:
                if not args.quiet:
                    file_str = '\033[1;35;40m {} '.format(item[0])
                    item_str = '\033[1;37;40m {}'.format(item[1])
                    sys.stdout.write('{}\t{}'.format(file_str, item_str)

    elif not args.quiet:
        sys.stdout.write('No matches found in {} for {}\n'.format(args.file, args.pattern))