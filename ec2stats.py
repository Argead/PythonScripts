#!/usr/bin/python3
"""
CLI script to get stats for currently running EC2 instances and print them to console.
"""

import boto3

def get_aws_credentials():
    aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    return aws_access_key_id, aws_secret_access_key
    
def dict_iterator(dictionary):
    for key in dictionary:
        if type(dictionary[key]) == list:
            print('\n'+key)
            for item in dictionary[key]:
                if type(item) in (list, dict):
                    dict_iterator(item)
                else:
                    line = '{}: {}'.format(key, item)
                    print(line)
        elif type(dictionary[key]) == dict:
            print('\n'+key)
            dict_iterator(dictionary[key])
        else:
            line = '{}: {}'.format(key, dictionary[key])
            print(line)
    
def get_ec2_stats():
    aws_access_key_id, aws_secret_access_key = get_aws_credentials()
    ec2 = boto3.client(
        'ec2',
        asw_access_key_id,
        aws_secret_access_key
    )
    try:
        response1 = ec2.describe_instances()
        print('INSTANCES')
        dict_iterator(response['Reservations']['Instances'])
        response2 = ec2.describe_instance_status()
        print('\n\nINSTANCE STATUS')
        dict_iterator(response2)
    except Exception as e:
        print(e)
    
if __name__ == '__main__':
    get_ec2_stats()