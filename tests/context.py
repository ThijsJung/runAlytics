import os
import sys

sys.path.insert(0, os.path.abspath('src'))

os.environ.update(**{
    'RUNS_TABLE': 'dummy-table'
})

from fit_parser import FITParser, Uploader