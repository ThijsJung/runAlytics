import os
import sys

sys.path.insert(0, os.path.abspath('src'))

os.environ.update(**{
    'RUNS_TABLE': 'dummy-table'
})

import mapper