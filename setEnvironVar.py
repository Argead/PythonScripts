#!/usr/bin/python3
"""
Set an environment variable from the command line.
"""
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('key', type=str, help="Key name for envrionment variable")
parser.add_argument('value',type=str, help="Value for the environment variable")
args = parser.parse_args()

KEY = args.key
VALUE = args.value

os.environ[KEY] = VALUE
print('Environment variable {} set to {}'.format(KEY, VALUE))
