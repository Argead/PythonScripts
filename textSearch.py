#!/usr/bin/python3
"""
Grep-like CLI utility written in Python.
"""
import argparse
import re


parser = argparse.ArgumentParser(description='Utility for searching document strings.')
parser.add_argument('string', type=str, help='Text that you want to search for in the document.')
parser.add_argument('file', type=str, help='The file that you want to search.')
parser.add_argument('-v', '--verbose', action='store_true', help='Print the line the search term was found on, rather than printing the line number.')
parser.add_argument('-e', '--exact', action='store_true', help='Search for only the exact word provided. If not specified, the script will find all matching character instances.')
args = parser.parse_args()


def search_file():
    linecount = 0
    instances = 0
    the_file = open(args.file, 'r')
    while True:
        next_line =  the_file.readline()
        if not next_line:
            if instances == 0:
                print('No instances of \"{}\" were found in {}.'.format(args.string, args.file))
            break
        linecount += 1
        if args.exact:
            pattern = ' ' + args.string + ' '
            if re.search(pattern, next_line):
                if args.verbose:
                    print(next_line)
                else:
                    print('\"{}\" was found on line {}.'.format(args.string, linecount))
                instances += 1
        elif args.string in next_line:
            if args.verbose:
                print(next_line)
            else:
                print('\"{}\" was found on line {}.'.format(args.string, linecount))
            instances += 1
    the_file.close()


if __name__ == '__main__':
    search_file()
