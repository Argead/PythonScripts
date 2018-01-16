#!/usr/bin/python3
"""
Script to upload files to an aws s3 instance using a three step process:
1.Verify that the bucket exists. Create it if not.
2.Upload the file to the bucket.
3.List the bucket contents to ensure that the file is found among them.
"""
import boto3
import os


def get_aws_credentials():
    aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    return aws_access_key_id, aws_secret_access_key


def upload_file_to_s3(bucket, targetFile):
    aws_access_key_id, aws_secret_access_key = get_aws_credentials()
    #create s3 client
    s3 = boto3.client(
        's3',
        aws_access_key_id = aws_access_key_id,
        aws_secret_access_key = aws_secret_access_key
    )
    bucket_name = bucket
    file_to_upload = targetFile
    buckets = s3.list_buckets()
    buckets_list = [bucket['Name'] for bucket in buckets['Buckets']]
    if not bucket_name in bucket_list:
        s3.create_bucket(Bucket=bucket_name)
    try:
        #Upload file
        s3.upload_file(file_to_upload,  bucket_name, file_to_upload)
    except:
        print('Error uploading file')
    #List the objects in the bucket
    current_objects = s3.list_objects(Bucket=bucket_name)
    if not file_to_upload in current_objects:
        print('File upload unsuccessful')
    else:
        print('File upload completed')



if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('bucket', type=str, help='bucket to upload file to')
    parser.add_argument('file', type=str, help='file you want to upload to s3')
    args = parser.parse_args()
    upload_file_to_s3(args.bucket, args.file)
