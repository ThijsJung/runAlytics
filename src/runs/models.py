from datetime import datetime
from typing import NamedTuple


class Run(NamedTuple):
    id: str
    created_at: datetime = None
    data: dict = {
        "distances": [],
        "heart_rates": [],
        "coordinates": [],
        "timestamps": []
    }

    def to_dict(self):
        return self._asdict()
