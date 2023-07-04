import unittest

from src.BeatmapData import _General, _Editor, _Metadata, _Difficulty, BeatmapData
from src.BeatmapFileParser import BeatmapFileParser
from src.constants import general_expected_slots, editor_expected_slots, metadata_expected_slots, \
    difficulty_expected_slots


class TestSlots(unittest.TestCase):
    def test_slots(self):
        cls_list = [_General, _Editor, _Metadata, _Difficulty]
        expected_slots_list = [general_expected_slots, editor_expected_slots, metadata_expected_slots,
                               difficulty_expected_slots]

        for (cls, expected_slots) in zip(cls_list, expected_slots_list):
            self.assertEqual(list(cls.__slots__), list(expected_slots))


class TestBeatmapFileParser(unittest.TestCase):
    def test_not_std_gamemode_file(self):
        input_file_path = "input_files/DJ Mendez - Tequila (Krisom) [lepidon! - Taiko Oni].osu"
        self.assertIsNone(BeatmapFileParser.parse_full_osu_file(input_file_path))

    def test_std_gamemode_file(self):
        input_file_path = "input_files/FELT - Day and Night (UndeadCapulet) [Terrace Ballad].osu"
        self.assertIsNotNone(BeatmapFileParser.parse_full_osu_file(input_file_path))

    def test_invalid_osu_files(self):
        invalid_file_paths = [
            "input_files/invalid_file_1.osu",
            "input_files/invalid_file_2.osu"
        ]

        for input_file_path in invalid_file_paths:
            try:
                result = BeatmapFileParser.parse_full_osu_file(input_file_path)
            except (KeyError, OSError, FileNotFoundError):
                return

            self.assertIsInstance(result, dict)
            self.assertDictEqual(result, {})


class TestBeatmapData(unittest.TestCase):
    def test_parse_full(self):
        input_file_path = "input_files/FELT - Day and Night (UndeadCapulet) [Terrace Ballad].osu"
        data = BeatmapData(BeatmapFileParser.parse_full_osu_file(input_file_path))
        self.assertIsNotNone(data)

    def test_parse_metadata(self):
        input_file_path = "input_files/FELT - Day and Night (UndeadCapulet) [Terrace Ballad].osu"
        data = BeatmapData(BeatmapFileParser.parse_osu_file_metadata(input_file_path))
        self.assertIsNotNone(data)

    def test_empty_initialized_data(self):
        data = BeatmapData.empty_initialized_beatmap_data()
        self.assertIsNotNone(data)

    def test_empty_data(self):
        data = BeatmapData.empty_beatmap_data()
        self.assertIsNotNone(data)


def all_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestSlots('Test_slots'))
    test_suite.addTest(TestBeatmapFileParser('Test_BeatmapFileParser'))
    test_suite.addTest(TestBeatmapData('Test_BeatmapData'))
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(all_suite())
