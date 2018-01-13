#!/usr/bin/python3


def db_login(database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    return connection, cursor

def show_format(records, sept):
    print(len(records), 'records')
    print(sept)
    for record in records:
        max = max(len(key) for key in record)
        for key in record:
            print('{} : {}'.format(max - key, record[key]))
        print(sept)
        
def dump_database(cursor, table):
    command = 'select * from {}'.format(table)
    cursor.execute(command)
    while True:
        record = cursor.fetchone()
        if not record:
            break
        print(record)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('database', type=str)
    parser.add_argument('table', type=str)
    args = parser.parse_args()
    connection, cursor = db_login(args.database)
    dump_database(cursor, args.table)
    