#!/usr/bin/python3

import boto3


def list_rds_instances():
    rds = boto3.client('rds')
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
    rds = boto3.client('rds')
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
    rds = boto3.client('rds')
    try:
        response = rds.delete_db_instance(
            DBInstanceIdentifier=database,
            SkipFinalSnapshot=True
        )
        print(response)
    except Exception as e:
        print(e)