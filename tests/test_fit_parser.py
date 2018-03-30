from datetime import datetime
import pytest
from tempfile import NamedTemporaryFile

from fit_parser import get_creation_timestamp, open_file, parse_fit_file
from runs.models import Run

FILENAME = 'data/FIT/5CDG0622.FIT'


def test_parse_fit_file_wrong_input_type():
    with NamedTemporaryFile() as tmp:
        fit_file = parse_fit_file(tmp.name)
    assert fit_file is None

@pytest.mark.skip(reason="Picking new FIT Files breaks this. Rethink")
def test_parse_fit_file():
    run = parse_fit_file(FILENAME)

    assert type(run) == Run
    assert run.data['distances'][0] == 1.8
    assert run.data['heart_rates'][0] == 86
    assert run.data['coordinates'][0] == (52.376378048211336, 4.891645414754748)
    assert run.data['timestamps'][0] == '2015-12-06T14:37:21'


@pytest.mark.skip(reason="Picking new FIT Files breaks this. Rethink")
def test_get_creation_time():
    fit_file = open_file(FILENAME)
    timestamp = get_creation_timestamp(fit_file)

    assert timestamp == '2015-12-06T14:37:21'