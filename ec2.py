#!/usr/bin/python3

import boto3

def list_instances():
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        print('Instance ID: {}\nInstance State:{}\n\n'.format(instance.id, instance.state))

def create_instance(imageID, minCount, maxCount, instanceType):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(imageID, minCount, maxCount, instanceType)
    print('New instance ID: {}'.format(instance[0].id))

def end_instance(instances=[]):
    ec2 = boto3.resource('ec2')
    for instance_id in instances:
        instance = ec2.Instance(instance_id)
        response = instance.terminate()
        print(response)


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
    
    elif args.mode == 'add':
    
    elif args.mode == 'delete':
    


