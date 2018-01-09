#!/usr/bin/env python3
"""
Simplified version of grep utility written in Python.
"""
import argparse
import os
import re
import sys


def grep(pattern, file):
    matches = []
    try:
        re_pattern = re.compile(pattern)
    except re.error:
        sys.stderr.write('Error - invalid regex pattern: ')
        sys.stderr.write('{}\n'.format(sys.exc_info()[1]))
        return matches
    try:
        if not os.path.exists(file):
            sys.stdout.write('Error: file does not exist\n')
            return matches
        if os.path.isfile(file):
            with open(file, 'r') as target:
                for line in target.readlines():
                    if re_pattern.search(line):
                        matches.append(line)
        elif os.path.isdir(file):
            #TODO: implement logic and option flags for parsing directory
            #each match will be a 2-item tuple of filename and matching line

    except re.error as e:
        sys.stderr.write(e)
        sys.stderr.write('{}\n'.format(sys.exc_info()[1]))
    return matches


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern', type=str, help='regex pattern to match')
    parser.add_argument('file', type=str, help='file to search')
    args = parser.parse_args()
    result = grep(args.pattern, args.file)
    if len(result) > 0:
        for item in result:
            if type(item) != tuple:
                file_str = '\033[1;35;40m {} '.format(args.file)
                item_str = '\033[1;37;40m {}'.format(item)
                sys.stdout.write('{}\t{}'.format(file_str, item_str))
            else:
                #TODO: implement output logic for directory grepping
        
            
    else:
        sys.stdout.write('No matches found in {} for {}\n'.format(args.file, args.pattern))