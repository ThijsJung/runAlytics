import boto3

from fit_parser import parse_fit_file
from runs.managers import FITManager, RunsManager
from runs.models import Run

runs_table =  boto3.resource('dynamodb').Table('runalytics')
fit_bucket = boto3.client('s3')

def parse_uploaded_fit_file(event, context):
    runs_manager = RunsManager(runs_table)
    fit_manager = FITManager(fit_bucket)

    if 'Records' in event:      # event is triggered by S3
        for record in event['Records']:
            # Fetch uploaded FIT file from S3
            fit_file = fit_manager.get(record)
            
            # Parse FitFile
            parsed_fit_file = parse_fit_file(fit_file)
            run = Run(
                id=record['s3']['object']['key'],
                created_at=parsed_fit_file['created_at'],
                data=parsed_fit_file['data']
            )
            
            # Save Run
            runs_manager.save(run)
