from dataclasses import dataclass


@dataclass
class SliderObject:
    __slots__ = ("length", "time")
    length: float
    time: int
