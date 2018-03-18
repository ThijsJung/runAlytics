import json

import boto3

from runs.models import Run
from utils import DecimalEncoder


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
