#!/usr/bin/python3
"""
CLI script to generate simple, incremental serial numbers for prototypes, components, and tests.
"""
import argparse
import datetime
import shelve
import sys

parser = argparse.ArgumentParser(description='Generate new serial numbers.')
parser.add_argument('mode', choices=['config', 'generate'], type=str, help='Either create a configuration file for the serial number generator, or generate a serial number.')
parser.add_argument('-o', '--override', action='store_true', help='If running the script in config mode, override any existing configuration file without a second prompt to the caller or user.')
parser.add_argument('-t', '--type', choices=['prototype', 'component', 'experiment'], type=str, help='If running the script in generate mode, choose the type of serial number to generate. Defaults to prototype.', default='prototype')
args = parser.parse_args()


def create_config_shelve():
    #TODO: Check if there is already a config file in CWD. If so, either check args or prompt user for overwrite permsision.
    with shelve.open('serial_config') as config:
        config_obj = {
            'prototype': {
                'current': '00000001',
                'increment': 1,
                'total_issued': 0
            },
            'component': {
                'current': '0000000001',
                'increment': 1,
                'total_issued': 0
            },
            'experiment': {
                'current': '000001',
                'increment': 1,
                'total_issued': 0
            }
        }
        config['default'] = config_obj
        
    print('Configuration complete')

    
def generate_serial_number():
    year = str(datetime.datetime.now().year)[2:]
    month = str(datetime.datetime.now().month)
    if len(month) < 2:
        month = '0' + month
    date = str(datetime.datetime.now().day)
    if len(date) < 2:
        date = '0' + date
    datestamp = year + month + date
    with shelve.open('serial_config') as config:
        last_serial = config['default'][args.type]['current']
        last_serial = int(last_serial)
        last_serial += config['default'][args.type]['increment']
        last_serial = str(last_serial)
        while len(last_serial) < len(config['default'][args.type]['current']):
            last_serial = '0' + last_serial
        new_serial = datestamp + args.type[0].upper() + last_serial
        print('New {} serial number: {}'.format(args.type.capitalize(), new_serial))
        config['default'][args.type]['current'] = new_serial
    

if __name__ == '__main__':
    if args.mode == 'config':
        create_config_shelve()
    elif args.mode == 'generate':
        generate_serial_number()