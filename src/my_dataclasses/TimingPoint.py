from dataclasses import dataclass


@dataclass
class TimingPoint:
    __slots__ = ("time", "beat_length", "meter", "sample_set", "sample_index", "volume", "uninherited", "effects")
    time: int
    beat_length: float
    meter: int
    sample_set: int
    sample_index: int
    volume: int
    uninherited: bool
    effects: int

    def __str__(self):
        return f"{self.time},{self.beat_length},{self.meter},{self.sample_set},{self.sample_index}," \
               f"{self.volume},{(int(self.uninherited))},{self.effects}"

    # TODO:
    #  Getters, setters?
