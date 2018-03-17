from runs.models import Run

def test_defaults():
    FIT_id = 'test_id'
    run_data = {
        "distances": [],
        "heart_rates": [],
        "coordinates": [],
        "timestamps": []
    }
    run = Run(id=FIT_id, **run_data)

    assert type(run) == Run
    assert run.id == 'test_id'
    assert run.heart_rates == []
    assert run.distances == []
    assert run.coordinates == []
    assert run.timestamps == []

def test_to_dict():
    FIT_id = 'test_id'
    run_data = {
        "distances": [],
        "heart_rates": [],
        "coordinates": [],
        "timestamps": []
    }
    run = Run(id=FIT_id, **run_data)

    assert run.to_dict() == dict(
        id='test_id',
        **run_data
    )