from functools import cached_property
from typing import Any, Dict, Mapping, List

from .constants import *
from .my_dataclasses.Event import Event
from .my_dataclasses.TimingPoint import TimingPoint


def _merge_dicts(d1: Mapping, d2: Mapping) -> dict:
    """
    Merges two dictionaries.
    If both dictionaries have the same key, takes value from the first dictionary.
    """
    return {**d1, **{k: v for k, v in d2.items() if k not in d1}}


class _General:
    __slots__ = ('audio_filename', 'audio_lead_in', 'audio_hash', 'preview_time',
                 'countdown', 'sample_set', 'stack_leniency', 'mode',
                 'letterbox_in_breaks', 'story_fire_in_front', 'use_skin_sprites',
                 'always_show_playfield', 'overlay_position', 'skin_preference',
                 'epilepsy_warning', 'countdown_offset', 'special_style',
                 'widescreen_storyboard', 'samples_match_playback_rate')

    def __init__(self, data: Dict[str, str]):
        if not data:
            return
        data = _merge_dicts(data, default_general_dict)

        for key, value in data.items():
            setattr(self, convert_to_attr_name_dict[key], value)


class _Editor:
    __slots__ = ('bookmarks', 'distance_spacing', 'beat_divisor', 'grid_size', 'timeline_zoom')

    def __init__(self, data: Dict[str, str]):
        if not data:
            return
        data = _merge_dicts(data, default_editor_dict)

        for key, value in data.items():
            setattr(self, convert_to_attr_name_dict[key], value)


class _Metadata:
    __slots__ = ('title', 'title_unicode', 'artist', 'artist_unicode',
                 'creator', 'version', 'source', 'tags',
                 'beatmap_id', 'beatmap_set_id')

    def __init__(self, data: Dict[str, str]):
        # Note: Always create Metadata to avoid error in _prettified_str
        data = _merge_dicts(data, default_metadata_dict)

        for key, value in data.items():
            setattr(self, convert_to_attr_name_dict[key], value)


class _Difficulty:
    __slots__ = ("hp", "cs", "od", "ar", "slider_multiplier",
                 "slider_tick_rate")

    def __init__(self, data: Dict[str, str]):
        if not data:
            return
        data = _merge_dicts(data, default_difficulty_dict)

        for key, value in data.items():
            setattr(self, convert_to_attr_name_dict[key], value)


class _Events:
    __slots__ = "background_filename"

    def __init__(self, data: List[Event]):
        if not data:
            return

        for event in data:
            if event.type:
                setattr(self, "background_filename", event.params[0][1:-1])  # "bg.png" -> bg.png
                break


class BeatmapData:
    """
    Class that stores Beatmap data. Wraps data from BeatmapFileParser.
    Created using example of an osu file format v14 file.
    """

    def __init__(self, data: Mapping[str, Any], *, filepath: str = ""):
        self.filepath = filepath
        self.datadict = _merge_dicts(data, empty_data_dict)

        self.general = _General(self.datadict["General"])
        self.editor = _Editor(self.datadict["Editor"])
        self.metadata = _Metadata(self.datadict["Metadata"])
        self.difficulty = _Difficulty(self.datadict["Difficulty"])
        self.events = _Events(self.datadict["Events"])
        self.timing_points: List[TimingPoint] = self.datadict["TimingPoints"]
        self.colours: List[List[str]] = self.datadict["Colours"]
        self.hit_objects: List[List[str]] = self.datadict["HitObjects"]

        self._hash = hash(self.metadata)

    @classmethod
    def empty_beatmap_data(cls):
        """Returns empty BeatmapData object WITHOUT initialized values"""
        return cls(filepath="", data=empty_data_dict)

    @classmethod
    def empty_initialized_beatmap_data(cls):
        """Returns empty BeatmapData object WITH ALL initialized values"""
        return cls(filepath="None", data=empty_initialized_data_dict)

    @cached_property
    def prettified_str(self) -> str:
        """
        Returns a prettified string that represents data about beatmap.
        The format of the string is:
        Artist - Song name [Diff name] (Mapper nickname)
        """
        return "{} - {} [{}] ({})".format(
            self.metadata.artist, self.metadata.title,
            self.metadata.version, self.metadata.creator)

    def __str__(self):
        return self.prettified_str

    def __hash__(self):
        return self._hash
