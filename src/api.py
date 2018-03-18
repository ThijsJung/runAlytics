import boto3

from runs.managers import RunsManager
from fit_parser import parse_fit_file


def get_runs_metadata():
    pass


def get_run(run_id):
    pass


def delete_run(run_id):
    pass


def upload_run(event, context):
    def get_FIT_file(record):
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        fit_file = s3.get_object(Bucket=bucket, Key=key)['Body'].read()

        return fit_file

    dynamodb_table = boto3.resource('dynamodb').Table('runalytics')
    manager = RunsManager(dynamodb_table)

    if 'Records' in event:      # event is triggered by S3
        for record in event['Records']:
            # Fetch uploaded FIT file from S3
            fit_file = get_FIT_file(record)
            
            # Parse FitFile
            run = parse_fit_file(fit_file)

            # Save Run
            manager.save(run)

# def get_runs(event, context):
#     db_runs = table.scan(ProjectionExpression='run_id')
#     runs = list()
#     if db_runs['Items']:
#         runs = [run['run_id'] for run in db_runs['Items']]
#     body = json.dumps(runs)
#     return dict(statusCode=200, body=body, headers={'Access-Control-Allow-Origin': '*'})

# def get_run_data(event, context):
#     run_id = str(event['pathParameters']['run_id'])
#     run_data = table.get_item(Key={'run_id': run_id})
#     body = json.dumps(run_data, cls=DecimalEncoder)

#     return dict(statusCode=200, body=body, headers={'Access-Control-Allow-Origin': '*'})
