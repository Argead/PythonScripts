#!/usr/bin/python3
"""
CLI interface for working with serial number scripts.
"""
import argparse
from serial import *
from serialStorage import *


def create_and_store_serial(serial_type, name='', db_name='serial.db'):
    try:
        #Create new serial number. Create a config file if needed.
        if not test_for_config():
            create_config_shelve()
        new_serial = generate_serial_number(serial_type)
        #Check that the database exists. Create it if not.
        if not test_for_database(db_name):
            create_dtabase(db_name)        
        #add new serial number to the database
        add_record(db_name, serial_type, new_serial, name)
    except Exception as e:
        print(e)

def retrieve_serials_from_storage(db_name='serial.db', serial_type):
    try:
        serials = get_all_serialnumber(db_name, serial_type)
        if args.output == 'file':
            with open('serials.txt', 'w') as new_file:
                new_file.write(serials)
        elif args.output == 'console':
            print(serials)
        
    except Exception as e:
        print(e)

def get_serials_summary(db_name='serial.db', serial_type):
    try:
        result = summary_info(db_name, serial_type)
        print(result)
    except Exception as e:
        print(e)

        
        
        
        