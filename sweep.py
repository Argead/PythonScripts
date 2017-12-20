#!/usr/bin/python3
"""
Tool for recording, storing, and replacing file access log timestamps.
"""
import argparse
import datetime
import os
import re
import subprocess
import sys


parser = argparse.ArgumentParser()
parser.add_argument('mode', type=str, choices=['get', 'set'], help="Set scrit mode to get (save timestamps) or set (overwrite timestamps).")
parser.add_argument('-d', '--directory', type=str, help='Directory to collect timestamps in. Defaults to CWD.', default='.')
args = parser.parse_args()


months = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12'
}


def get_timestamps():
    if args.directory != os.getcwd():
        os.chdir(os.path.abspath(args.directory))
    if sys.platform[:3] == 'win':
        SHELL = False
    else:
        SHELL = True
    print('Collecting current time stamps...')
    tempfile = open('._tempfile', 'w')
    current_timestamps = subprocess.call('ls -l', shell=SHELL, stdout=tempfile)
    tempfile.close()
    print('Completed')

def set_timestamps():
    print('Resetting timestamps...')
    tempfile = open('._tempfile', 'r')
    timestamps = tempfile.readlines()
    timestamps.pop(0)
    pattern_to_remove = '^[-|r|w|x]{10}\s\d+\s[A-Za-z0-9]+\s[A-Za-z0-9]+\s+\d+\s+'    
    for line in timestamps:
        line = re.sub(pattern_to_remove, '', line)
        line = line.rstrip() #remove the newline character
        line = line.split(' ')
        if os.path.isfile(line[-1]):        
            hour_min_pattern = '\d{2}:\d{2}'
            if re.match(hour_min_pattern, line[2]) == None:
                #timestamp is for a previous year
                month = months[line[0]]
                new_timestamp = '{}-{}-{}'.format(line[4], month, line[2])
            else:
                #timestamp is for current year
                month = months[line[0]]
                year = datetime.datetime.now().year
                new_timestamp = '{}-{}-{} {}:00'.format(year, month, line[1], line[2])

            command = 'touch -d "{}" {}'.format(new_timestamp, line[-1])
            subprocess.call(command, shell=True)

    #delete the tempfile
    tempfile.close()
    subprocess.call('rm ._tempfile', shell=True)
    print('Reset Completed')    

if __name__ == '__main__':
    if args.mode == 'get':
        get_timestamps()
    elif args.mode == 'set':
        set_timestamps()
