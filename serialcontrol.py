#!/usr/bin/python3
"""
CLI interface for working with serial number scripts.
"""
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
        print(new_serial)
        add_record(db_name, serial_type, new_serial, name)
    except Exception as e:
        print(e)

def retrieve_serials_from_storage(serial_type, db_name='serial.db'):
    try:
        serials = get_all_serialnumber(db_name, serial_type)
        if args.output == 'file':
            with open('serials.txt', 'w') as new_file:
                new_file.write(serials)
        elif args.output == 'console':
            print(serials)
        
    except Exception as e:
        print(e)

def get_serials_summary(serial_type, db_name='serial.db'):
    try:
        result = summary_info(db_name, serial_type)
        print(result)
    except Exception as e:
        print(e)

        
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', type=str, choices=['add', 'get', 'summary'], default='add', help='Mode to run script in. Add to add a new serial number to DB, get to retrieve all serial numbers of a specified type, summary for summary data on a serial type. Defaults to add.')
    parser.add_argument('-d', '--database', default='serial.db', type=str, help='Database name. Defaults to serial.db.')
    parser.add_argument('-t', '--type', choices=['prototype', 'component', 'experiment'], default='prototype', type=str, help='Choose type of serial number to create and add to DB. Defaults to prototype.')
    parser.add_argument('-n', '--name', type=str, default='', help='Optional name to associate with new serial number. Use with add mode. Defaults to empty string.')
    args = parser.parse_args()
    
    if args.mode == 'add':
        create_and_store_serial(args.type, args.name, args.database)
    elif args.mode == 'get':
        retrieve_serials_from_storage(args.type, args.database)
    elif args.mode == 'summary':
        get_serials_summary(args.type, args.database)
        