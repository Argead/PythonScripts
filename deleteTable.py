#!/usr/bin/python3

import sys

def db_login(database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    return connection, cursor  

def clear_table(database, table):
    connection, cursor = db_login(database, table)
    if input('Confirm you want to proceed;').lower() not in ('y', 'yes', 'c', 'confirm'):
        return
    try:
        command = 'delete from {}'.format(table)
        cursor.execute(command)
        connection.commit()
        print('job completed')
    except:
        print('job could not be completed')
        sys.exit()

if __name__ == '__main__':
    import argparse
    parser = argpase.ArgumentParser()
    parser.add_argument('database', type=str, help='database housing the table you want to empty')
    parser.add_argument('table', type=str, help='name of the table that you want to empty')
    args = parser.parse_args()