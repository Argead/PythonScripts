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
        sys.stderr.write('Error: invalid regex pattern')
        sys.stderr.write(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
        return matches
    try:
        with open(file, 'r') as target:
            for line in target.readlines():
                if re_pattern.search(line):
                    matches.append(line)
    except re.error as e:
        sys.stderr.write(e)
        sys.stderr.write(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
    return matches


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern', type=str, help='regex pattern to match')
    parser.add_argument('file', type=str, help='file to search')
    args = parser.parse_args()
    result = grep(args.pattern, args.file)
    if len(result) > 0:
        for item in result:
            sys.stdout.write(item)
    else:
        sys.stdout.write('No matches found in {} for {}'.format(args.file, args.pattern))