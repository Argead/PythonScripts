#!/usr/bin/python3

import pylint
import pycodestyle
import pydocstyle
import subprocess

def lint(target_file):
    lint1 = subprocess.Popen(['pylint', target_file], stdout=subprocess.PIPE)
    lint1.communicate()[0]

    

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()


    args = parser.parse_args()

