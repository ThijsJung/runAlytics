from unittest.mock import Mock

import boto3
import pytest

from runs.managers import RunsManager
from runs.models import Run

mock_dynamodb_table = Mock(spec=boto3.resource(
    'dynamodb').Table('test-table-name'))
mock_s3_resource = Mock(spec=boto3.client('s3'))

class TestRunsManager:
    def test_save(self):
        manager = RunsManager(mock_dynamodb_table)
        run = Run(id='test_id')

        manager.save(run)

        mock_dynamodb_table.put_item.assert_called_with(
            Item='{"id": "test_id", "created_at": null, "data": {"distances": [], "heart_rates": [], "coordinates": [], "timestamps": []}}'
        )


    def test_delete(self):
        manager = RunsManager(mock_dynamodb_table)

        manager.delete('test_id')

        mock_dynamodb_table.delete_item.assert_called_once_with(
            Key='test_id'
        )


    def test_get(self):
        manager = RunsManager(mock_dynamodb_table)
        mock_dynamodb_table.get_item.return_value = {'id': 'test_id'}

        run = manager.get('test_id')

        mock_dynamodb_table.get_item.assert_called_with(
            Key='test_id'
        )
        assert run == Run('test_id')

class TestFITManager:
    @pytest.mark.skip(reason="Must write tests")
    def test__generate_key(self):
        pass
    
    @pytest.mark.skip(reason="Must write tests")
    def test_save(self):
        pass
    
    @pytest.mark.skip(reason="Must write tests")
    def test_get(self, key):
        pass
