# OsuFileParser
[![GitHub release](https://img.shields.io/github/release/ZyMa-1/OsuFileParser.svg?style=for-the-badge&logo=github)](https://github.com/ZyMa-1/OsuFileParser/releases/latest)
<br>
<br>
[![Python Version](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-310/)
[![Licence MIT](https://img.shields.io/badge/License-MIT-purple.svg)](/LICENCE)
![Test Status](https://github.com/ZyMa-1/OsuFileParser/actions/workflows/tests.yml/badge.svg?branch=master)

Package for wrapping ".osu" file data into a python class.

## Simple usage

```python
from OsuFileParser import BeatmapFileParser, BeatmapData

input_file_path = "input_files/FELT - Day and Night (UndeadCapulet) [Terrace Ballad].osu"

beatmap_data = BeatmapData(BeatmapFileParser.parse_full_osu_file(input_file_path))
print("Beatmap data as a string:", str(beatmap_data))
print("Beatmap title unicode:", beatmap_data.metadata.title_unicode)
print("Beatmap cs:", beatmap_data.difficulty.cs)
print("Beatmap od:", beatmap_data.difficulty.od)
print("Beatmap hp:", beatmap_data.difficulty.hp)
```

See `examples` folder for more [examples](/examples).

## How to download

Add following dependency to your `requirements.txt` file:
```
git+https://github.com/ZyMa-1/OsuFileParser.git@latest
```