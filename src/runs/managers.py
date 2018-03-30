import json
from tempfile import NamedTemporaryFile

import boto3

from runs.models import Run
from utils import DecimalEncoder

class FITManager():
    prefix = 'FIT_files'

    def __init__(self, s3_client):
        self.s3_client = s3_client
    
    def _generate_key(self, fit_id):
        return f"{self.prefix}/{fit_id}"
    
    def save(self, fit_file):
        pass
    
    def get(self, record: dict) -> bytes:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        fit_file = self.s3_client.get_object(
            Bucket=bucket,
            Key=self._generate_key(key)
        )['Body'].read()

        return fit_file


class RunsManager():
    def __init__(self, boto3_dynamodb_table):
        self.table = boto3_dynamodb_table

    def save(self, run: Run) -> None:
        self.table.put_item(
            Item=json.dumps(run.to_dict(), cls=DecimalEncoder)
        )

    def delete(self, run_id: str) -> None:
        self.table.delete_item(
            Key=run_id
        )

    def get(self, run_id: str) -> Run:
        run_data = self.table.get_item(
            Key=run_id
        )
        return Run(**run_data)
