#!/usr/bin/python3

import sqlite3


def db_login(database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    return connection, cursor

def load_db(cursor, table, file, connection):
    source = open(file)
    rows = [line.rstrip().split(',') for line in source]
    rows = [str(tuple(reccord)) for record in rows]
    for item in rows:
        cursor_command = 'insert into {} values {}'.format(table, item)
        cursor.execute(cursor_command)
    if connection:
        connection.commit()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('database', type=str, help='database name')
    parser.add_argument('table', type='str', help='database table to add records to')
    parser.add_argument('source', type=str, help='source csv file')
    connection, cursor = db_login(args.database)
    load_db(cursor, args.table, args.source, connection)