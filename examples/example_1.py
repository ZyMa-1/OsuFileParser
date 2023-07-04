from src.BeatmapData import BeatmapData
from src.BeatmapFileParser import BeatmapFileParser

input_file_path = "input_files/FELT - Day and Night (UndeadCapulet) [Terrace Ballad].osu"

beatmap_data = BeatmapData(BeatmapFileParser.parse_full_osu_file(input_file_path))
print("Beatmap data as a string:", str(beatmap_data))
print("Beatmap title unicode:", beatmap_data.metadata.title_unicode)
print("Beatmap cs:", beatmap_data.difficulty.cs)
print("Beatmap od:", beatmap_data.difficulty.od)
print("Beatmap hp:", beatmap_data.difficulty.hp)
