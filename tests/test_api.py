from unittest.mock import Mock, patch

import boto3

from api import upload_run

mock_dynamodb_table = Mock(spec=boto3.resource(
    'dynamodb').Table('test-table-name'))

@patch('api.RunsManager.save')
def test_upload_run(mock_save_run):
    fit_file = 'data/FIT/ghjk'

    event = {
        "Records": [
            {
                "s3": {
                    "bucket": {"name" : "test_bucket"},
                    "object": {"key": "test_key"}
                }
            }]
    }

    print("NEXT UP: IMPLEMENT MANAGER FOR FIT FILES")
    upload_run(event, {})

    mock_save_run.assert_called_once()
