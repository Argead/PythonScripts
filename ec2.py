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





