import decimal
import os
import json

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['RUNS_TABLE'])

class DecimalEncoder(json.JSONEncoder):
    """Helper class to convert a DynamoDB item to JSON."""

    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)

def get_runs(event, context):
    db_runs = table.scan(ProjectionExpression='run_id')
    runs = list()
    if db_runs['Items']:
        runs = [run['run_id'] for run in db_runs['Items']]
    body = json.dumps(runs)
    return dict(statusCode=200, body=body, headers={'Access-Control-Allow-Origin': '*'})

def get_run_data(event, context):
    run_id = str(event['pathParameters']['run_id'])
    run_data = table.get_item(Key={'run_id': run_id})
    body = json.dumps(run_data, cls=DecimalEncoder)

    return dict(statusCode=200, body=body, headers={'Access-Control-Allow-Origin': '*'})