from datetime import datetime
from uuid import uuid4

from typing import NamedTuple, List

class Run(NamedTuple):
    id: str
    timestamps: list
    coordinates: list
    distances: list
    heart_rates: list


    def to_dict(self):
        return self._asdict()

