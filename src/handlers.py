import os
import boto3

from fit_parser import Uploader, FITParser

s3 = boto3.client('s3')


def handler(event, context):
    uploader = Uploader(FITParser())
    if 'Records' in event:      # event is triggered by S3
        for record in event['Records']:
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            fit_file = s3.get_object(Bucket=bucket, Key=key)['Body'].read()
            uploader.run(fit_file)
