from dataclasses import dataclass
from typing import List


@dataclass
class Event:
    type: str | int
    start_time: int
    params: List[str]
