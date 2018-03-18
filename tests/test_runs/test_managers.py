from unittest.mock import Mock

import boto3

from runs.managers import RunsManager
from runs.models import Run

mock_dynamodb_table = Mock(spec=boto3.resource(
    'dynamodb').Table('test-table-name'))


def test_manager_save():
    manager = RunsManager(mock_dynamodb_table)
    run = Run(id='test_id')

    manager.save(run)

    mock_dynamodb_table.put_item.assert_called_with(
        Item='{"id": "test_id", "created_at": null, "data": {"distances": [], "heart_rates": [], "coordinates": [], "timestamps": []}}'
    )


def test_manager_delete():
    manager = RunsManager(mock_dynamodb_table)

    manager.delete('test_id')

    mock_dynamodb_table.delete_item.assert_called_once_with(
        Key='test_id'
    )


def test_manager_get():
    manager = RunsManager(mock_dynamodb_table)
    mock_dynamodb_table.get_item.return_value = {'id': 'test_id'}

    run = manager.get('test_id')

    mock_dynamodb_table.get_item.assert_called_with(
        Key='test_id'
    )
    assert run == Run('test_id')
