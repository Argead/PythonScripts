#!/usr/bin/python3

import boto3
import botocore
import os
import sys

def get_aws_credentials():
    aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    return aws_access_key_id, aws_secret_access_key

def download_file_from_s3(bucket, key, local_file):
    aws_access_key_id, aws_secret_access_key = get_aws_credentials()
    #TODO: boto3.client or boto3.resource ?
    s3 = boto3.client(
        's3',
        aws_access_key_id,
        aws_secret_access_key
    )
    try:
        s3.Bucket(bucket).download_file(key, local_file)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
            print('Requested object does not existing in this bucket: {}'.format(bucket))
            sys.exit()
        else:
            raise
            
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('bucket', type=str, help='bucket containing the file you want to download from s3')
    parser.add_argument('key', type=str, help='s3 key associated with the file you want to download')
    parser.add_argument('filename', type=str, help='name of file you want to download to')
    args = parser.parse_args()
    download_file_from_s3(args.bucket, args.key, args.filename)