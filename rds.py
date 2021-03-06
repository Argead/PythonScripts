#!/usr/bin/python3

import boto3

def get_aws_credentials():
    aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    return aws_access_key_id, aws_secret_access_key

def list_rds_instances():
    aws_access_key_id, aws_secret_access_key = get_aws_credentials()
    rds = boto3.client(
        'rds',
        asw_access_key_id,
        aws_secret_access_key
    )
    try:
        dbs = rds.describe_db_instances()
        for db in dbs['DBInstances']:
            print('{}@{}:{} {}'.format(
                db['MasterUsername'],
                db['Endpoint']['Address'],
                db['Endpoint']['Port'],
                db['DBInstanceStatus']
            ))
    except Exception as e:
        print(e)

def create_rds_instance(identifier, masterUsername, masterUserPassword, dbInstanceClass, engine, allocatedStorage):
    aws_access_key_id, aws_secret_access_key = get_aws_credentials()
    rds = boto3.client(
        'rds',
        asw_access_key_id,
        aws_secret_access_key
    )
    try:
        instance = rds.create_db_instance(
            DBInstanceIdentifier=identifier,
            MasterUsername=masterUsername,
            MasterUserPassword=masterUserPassword,
            DBInstanceClass=dbInstanceClass,
            Engine=engine,
            AllocatedStorage=allocatedStorage)
        print(instance)
    except Exception as e:
        print(e)
        
def end_rds_instance(database):
    aws_access_key_id, aws_secret_access_key = get_aws_credentials()
    rds = boto3.client(
        'rds',
        asw_access_key_id,
        aws_secret_access_key
    )
    try:
        response = rds.delete_db_instance(
            DBInstanceIdentifier=database,
            SkipFinalSnapshot=True
        )
        print(response)
    except Exception as e:
        print(e)
        
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['list', 'add', 'delete'],type=str, help='choose mode to run script in from command line')
    parser.add_argument('--identifier', type=str, help='DBInstanceIdentifier; use only with add mode')
    parser.add_argument('--masterUsername', type=str, help='MasterUsername; use only with add mode')
    parser.add_argument('--masterUserPassword', type=str, help='MasterUserPassword; use only with add mode')
    parser.add_argument('--dbInstanceClass', type=str, help='DBInstanceClass; use only with add mode')
    parser.add_argument('--engine', type=str, help='Engine; use only with add mode')
    parser.add_argument('--allocatedStorage', type=int, help='AllocatedStorage; use only with add mode')
    parser.add_argument('--database', type=str, help='database to delete; use only with delete mode')
    args = parser.parse_args()
    if args.mode == 'list':
        list_rds_instances()
    elif args.mode == 'add':
        create_rds_instance(args.identifier, args.masterUsername, args.masterUserPassword, args.dbInstanceClass, args.engine, args.allocatedStorage)
    elif args.mode == 'delete':
        end_rds_instance(args.database)