from types import MappingProxyType

empty_data_dict: MappingProxyType[str, dict] = MappingProxyType({
    "General": {},
    "Editor": {},
    "Metadata": {},
    "Difficulty": {},
    "Events": {},
    "TimingPoints": {},
    "Colours": {},
    "HitObjects": {},
})

default_general_dict: MappingProxyType[str, str] = MappingProxyType({
    "AudioFilename": "None",
    "AudioLeadIn": "None",
    "AudioHash": "None",
    "PreviewTime": "None",
    "Countdown": "None",
    "SampleSet": "None",
    "StackLeniency": "None",
    "Mode": "None",
    "LetterboxInBreaks": "None",
    "StoryFireInFront": "None",
    "UseSkinSprites": "None",
    "AlwaysShowPlayfield": "None",
    "OverlayPosition": "None",
    "SkinPreference": "None",
    "EpilepsyWarning": "None",
    "CountdownOffset": "None",
    "SpecialStyle": "None",
    "WidescreenStoryboard": "None",
    "SamplesMatchPlaybackRate": "None",
})

default_editor_dict: MappingProxyType[str, str] = MappingProxyType({
    "Bookmarks": "None",
    "DistanceSpacing": "None",
    "BeatDivisor": "None",
    "GridSize": "None",
    "TimelineZoom": "None",
})

default_metadata_dict: MappingProxyType[str, str] = MappingProxyType({
    "Title": "None",
    "TitleUnicode": "None",
    "Artist": "None",
    "ArtistUnicode": "None",
    "Creator": "None",
    "Version": "None",
    "Source": "None",
    "Tags": "None",
    "BeatmapID": "None",
    "BeatmapSetID": "None",
})

default_difficulty_dict: MappingProxyType[str, str] = MappingProxyType({
    "HPDrainRate": "None",
    "CircleSize": "None",
    "OverallDifficulty": "None",
    "ApproachRate": "None",
    "SliderMultiplier": "None",
    "SliderTickRate": "None"
})

default_events_dict: MappingProxyType[str, str] = MappingProxyType({})

default_colours_dict: MappingProxyType[str, str] = MappingProxyType({})

general_expected_slots = ('audio_filename', 'audio_lead_in', 'audio_hash', 'preview_time',
                          'countdown', 'sample_set', 'stack_leniency', 'mode',
                          'letterbox_in_breaks', 'story_fire_in_front', 'use_skin_sprites',
                          'always_show_playfield', 'overlay_position', 'skin_preference',
                          'epilepsy_warning', 'countdown_offset', 'special_style',
                          'widescreen_storyboard', 'samples_match_playback_rate')
editor_expected_slots = ('bookmarks', 'distance_spacing', 'beat_divisor', 'grid_size', 'timeline_zoom')
metadata_expected_slots = ('title', 'title_unicode', 'artist', 'artist_unicode',
                           'creator', 'version', 'source', 'tags',
                           'beatmap_id', 'beatmap_set_id')
difficulty_expected_slots = ("hp", "cs", "od", "ar", "slider_multiplier",
                             "slider_tick_rate")

__temp_convert_to_attr_name_dict = {}

__temp_empty_initialized_data_dict = dict(empty_data_dict)
__temp_empty_initialized_data_dict["General"] = default_general_dict
__temp_empty_initialized_data_dict["Editor"] = default_editor_dict
__temp_empty_initialized_data_dict["Metadata"] = default_metadata_dict
__temp_empty_initialized_data_dict["Difficulty"] = default_difficulty_dict
empty_initialized_data_dict = MappingProxyType(__temp_empty_initialized_data_dict)

ALL_SECTION_NAMES = [
    "General",
    "Editor",
    "Metadata",
    "Difficulty",
    "Events",
    "TimingPoints",
    "Colours",
    "HitObjects"
]

OSU_GAMEMODE_VALUE: int = 0

for __ind, __key in enumerate(default_general_dict):
    __temp_convert_to_attr_name_dict[__key] = general_expected_slots[__ind]
for __ind, __key in enumerate(default_editor_dict):
    __temp_convert_to_attr_name_dict[__key] = editor_expected_slots[__ind]
for __ind, __key in enumerate(default_metadata_dict):
    __temp_convert_to_attr_name_dict[__key] = metadata_expected_slots[__ind]
for __ind, __key in enumerate(default_difficulty_dict):
    __temp_convert_to_attr_name_dict[__key] = difficulty_expected_slots[__ind]

convert_to_attr_name_dict: MappingProxyType[str, str] = MappingProxyType(__temp_convert_to_attr_name_dict)
