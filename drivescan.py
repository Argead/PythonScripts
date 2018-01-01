#!/usr/bin/python3
"""
CLI script to find the largest of a given file type in any directory.
"""
import os
import pprint
import sys

trace = 1
dirname = os.curdir
extension_name = '.py'
if len(argv) > 1: dirname = argv[1]
if len(argv) > 2: extension_name = argv[2]
if len(argv) > 3: trace   = int(argv[3])

def tryprint(arg):
    try:
        prnt(arg)
    except UnicodeEncodeError:
        print(arg.encode())

visited = set()
allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace:
        tryprint(thisDir)
    thisDir = os.path.normpath(thisDir)
    fixname = os.path.normcase(thisDir)
    if fixname in visited:
        if trace:
            tryprint('skipping ' + thisDir)
        else:
            visited.add(fixname)
            for filename in filesHere:
                if filename.endswith(extension_name):
                    if trace > 1:
                        tryprint('+++' + filename)
                    fullname = os.path.join(thisDir, filename)
                    try:
                        bytesize = os.path.getsize(fullname)
                        linesize = sum(+1 for line in open(fullname, 'rb'))
                    except Exception:
                        print('error', exc_info()[0])
                    else:
                        allsizes.append((bytesize, lnesize, fullname))

for (title, key) in [('bytes', 0), ('lines', 1)]:
    print('\nBy %s...' % title)
    allsizes.sort(key=lambda x: x[key])
    pprint.pprint(allsizes[:3])
    pprint.pprint(allsizes[-3:])
  
