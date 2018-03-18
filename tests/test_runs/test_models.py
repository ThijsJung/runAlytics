from runs.models import Run

def test_defaults():
    run = Run('test_id')

    assert type(run) == Run
    assert run.created_at is None
    assert run.data['heart_rates'] == []
    assert run.data['distances'] == []
    assert run.data['coordinates'] == []
    assert run.data['timestamps'] == []

def test_required_args():
    FIT_id = 'test_id'
    timestamp = 'fake-timestamp'

    run = Run(id=FIT_id, created_at=timestamp)

    assert run.created_at == timestamp

def test_to_dict():
    FIT_id = 'test_id'
    run = Run(FIT_id)

    assert run.to_dict() == dict(
        id=FIT_id,
        created_at=None,
        data=dict(
            distances=[],
            heart_rates=[],
            coordinates=[],
            timestamps=[])
    )