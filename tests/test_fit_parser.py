from fit_parser import parse_fit_file

import pytest

from runs.models import Run

FILENAME = 'data/FIT/5C6F3721.FIT'

def test_parse_fit_file_wrong_input_type():
    with pytest.raises(FileNotFoundError):
        fit_file = parse_fit_file('not a fit file')
    
def test_parse_fit_file():
    fit_file = parse_fit_file(FILENAME)

    assert type(fit_file) == Run

def test_get_run_id():
    pass
    
def test_get_creation_time():
    pass