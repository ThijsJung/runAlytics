from unittest.mock import Mock, patch

import boto3
import pytest

from handlers.parse_uploaded_fit_file import parse_uploaded_fit_file


def fit_file():
    fit_file = '/home/thijs/Projects/runalytics/data/FIT/5CDG0622.FIT'
    return open(fit_file, 'rb')


@pytest.fixture
def s3_put_object_event():
    event = {
        "Records": [
            {
                "s3": {
                    "bucket": {"name": "test_bucket"},
                    "object": {"key": "test_key"}
                }
            }]
    }

    return event


@patch('handlers.parse_uploaded_fit_file.runs_table')
@patch('handlers.parse_uploaded_fit_file.fit_bucket')
def test_upload_run(mock_fit_bucket, mock_runs_table, s3_put_object_event):
    mock_fit_bucket.get_object.return_value = dict(Body=fit_file())

    parse_uploaded_fit_file(s3_put_object_event, {})

    mock_fit_bucket.get_object.assert_called_with(
        Bucket="test_bucket",
        Key="FIT_files/test_key"
    )

    mock_runs_table.put_item.assert_called_once()
