#!/usr/bin/python3
"""
CLI interface for working with serial number scripts.
"""
import logging
import pprint
from serial import *
from serialStorage import *
from sys import stdout


logger = logging.getLogger('main_logger')
logger.setLevel(logging.INFO)
#create file handler for main_logger
fh = logging.FileHandler('serial.log')
fh.setLevel(logging.INFO)
fm = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(fm)


def create_and_store_serial(serial_type, name='', db_name='serial.db', printSerial=False):
    try:
        #Create new serial number. Create a config file if needed.
        if not test_for_config():
            create_config_shelve()
        new_serial = generate_serial_number(serial_type)
        #Check that the database exists. Create it if not.
        if not test_for_database(db_name):
            create_dtabase(db_name)        
        #Add new serial number to the database
        add_record(db_name, serial_type, new_serial, name)
        logger.info('new serial added to db: {}'.format(db_name))
    except Exception as e:
        logger.error(e)

def retrieve_serials_from_storage(serial_type, db_name='serial.db'):
    try:
        serials = get_all_serialnumbers(db_name, serial_type)
        if args.output == 'file':
            for record in serials:
                logger.info(record)
        elif args.output == 'console':
            print('INDEX, SERIAL, NAME')
            for record in serials:
                logger.info(record)
    except Exception as e:
        logger.error(e)

def get_serials_summary(serial_type, db_name='serial.db'):
    try:
        result = summary_info(db_name, serial_type)
        logger.info('{} {} serial numbers'.format(result, serial_type))
    except Exception as e:
        logger.error(e)

        
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', type=str, choices=['add', 'get', 'summary'], default='add', help='Mode to run script in. Add to add a new serial number to DB, get to retrieve all serial numbers of a specified type, summary for summary data on a serial type. Defaults to add.')
    parser.add_argument('-d', '--database', default='serial.db', type=str, help='Database name. Defaults to serial.db.')
    parser.add_argument('-t', '--type', choices=['prototype', 'component', 'experiment'], default='prototype', type=str, help='Choose type of serial number to create and add to DB. Defaults to prototype.')
    parser.add_argument('-n', '--name', type=str, default='', help='Optional name to associate with new serial number. Use with add mode. Defaults to empty string.')
    parser.add_argument('-o', '--output', type=str, choices=['file','console'], default='console', help='Choose to write output of db query to file serials.txt or to console. Defaults to console.')
    parser.add_argument('-p', '--print', action='store_true', default=False, help='Print the new serial number to stdout.')
    args = parser.parse_args()
    
    if args.mode == 'add':
        create_and_store_serial(args.type, args.name, args.database, args.print)
    elif args.mode == 'get':
        retrieve_serials_from_storage(args.type, args.database)
    elif args.mode == 'summary':
        get_serials_summary(args.type, args.database)
        