#!/usr/bin/python3


def db_login(database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    return connection, cursor  

def delete_table(database, table):
    connection, cursor = db_login(database)
    if input('Confirm you want to delete this table: ').lower() not in ('y', 'yes', 'c', 'confirm'):
        print('aborting job')
        return
    try:
        del_command = 'drop table {}'.format(table)
        cursor.execute(del_command)
    except:
        print('this table does not exist')
    make_command = 'create table {}'.format(table)
    cursor.execute(make_command)
    connection.commit()
    print('job completed')
    return
    

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Delete and replace an existing table in a SQL database.')
    parser.add_argument('database', type=str, help='database housing the table that you want to delete and recreate')
    parser.add_argument('table', type=str, help='table that you want to delete and recreate')
    args = parser.parse_args()
    
    delete_table(args.database, args.table)