# import logging
#
# from src.BeatmapData import _General, _Editor, _Metadata, _Difficulty
# from src.constants import general_expected_slots, editor_expected_slots, metadata_expected_slots, \
#     difficulty_expected_slots
#
# logger = logging.getLogger(__name__)
#
#
# def check_slots(cls_list: list, expected_slots_list: list):
#     for (cls, expected_slots) in zip(cls_list, expected_slots_list):
#         assert list(cls.__slots__) == list(expected_slots)
#
#
# check_slots([_General, _Editor, _Metadata, _Difficulty],
#             [general_expected_slots, editor_expected_slots, metadata_expected_slots, difficulty_expected_slots])
