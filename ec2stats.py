#!/usr/bin/python3

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
    
    


        
        
    

