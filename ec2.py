#!/usr/bin/python3

import boto3

def get_aws_credentials():
    aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    return aws_access_key_id, aws_secret_access_key

def list_instances():
    aws_access_key_id, aws_secret_access_key = get_aws_credentials()
    ec2 = boto3.client(
        'ec2',
        asw_access_key_id,
        aws_secret_access_key
    )
    try:
        for instance in ec2.instances.all():
            print('Instance ID: {}\nInstance State:{}\n\n'.format(instance.id, instance.state))
    except botocore.exceptions.ClientError as e:
        print(e)

def create_instance(imageID, minCount, maxCount, instanceType):
    aws_access_key_id, aws_secret_access_key = get_aws_credentials()
    ec2 = boto3.client(
        'ec2',
        asw_access_key_id,
        aws_secret_access_key
    )
    try:
        instance = ec2.create_instances(imageID, minCount, maxCount, instanceType)
        print('New instance ID: {}'.format(instance[0].id))
    except botocore.exceptions.ClientError as e:
        print(e)
        
def end_instance(instances=[]):
    aws_access_key_id, aws_secret_access_key = get_aws_credentials()
    ec2 = boto3.client(
        'ec2',
        asw_access_key_id,
        aws_secret_access_key
    )
    try:
        for instance_id in instances:
            instance = ec2.Instance(instance_id)
            response = instance.terminate()
            print(response)
    except botocore.exceptions.ClientError as e:
        print(e)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['list', 'add', 'delete'], type=str, help='choose mode to run this script in from the command line')
    parser.add_argument('-i', '--imageID', type=str, help='imageID; use with add mode.')
    parser.add_argument('-m', '--minCount', type=int, help='minimum number of instances to create; use with add mode')
    parser.add_argument('-x', '--maxCount', type=int, help='maximum number of instances to create; use with add mode')
    parser.add_argument('-t', '--type', type=str, help='type of instance to create; use with add mode')
    parser.add_argument('-l', '--listOfInstances', nargs='+', help='list the instances you want to delete; use with delete mode')
    args = parser.parse_args()
    if args.mode == 'list':
        list_instances()
    elif args.mode == 'add':
        create_instance(args.imageID, args.minCount, args.maxCount, args.type)
    elif args.mode == 'delete':
        end_instance(args.listOfInstances)