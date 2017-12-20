#!/usr/bin/python3
"""
Simple CLI paging utility.
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('text', help="the text file that you want to page.")
parser.add_argument('-n', '--number', help="the number of lines to print at a time.", default=20)
args = parser.parse_args()

affirmatives = ['y', 'Y', 'Yes']
text = open(args.file).read()
text = text.splitlines()
while text:
	blob = text[:args.number]
	remaining = text[args.number:]
	for line in blob:
		print(line)
	if text and input('Print more?') not in affirmatives:
		break

