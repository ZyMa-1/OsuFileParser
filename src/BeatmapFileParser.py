import logging
import pathlib
from typing import Dict, List, TextIO, Any

from .constants import ALL_SECTION_NAMES, OSU_GAMEMODE_VALUE
from .my_dataclasses.Event import Event
from .my_dataclasses.TimingPoint import TimingPoint

logger = logging.getLogger(__name__)


class _SectionParser:
    @staticmethod
    def parse_key_value_section(file_object: TextIO) -> Dict[str, str]:
        data_res = {}
        while 1:
            pos = file_object.tell()
            line = file_object.readline()
            if not line:
                break
            line = line.rstrip()
            if line.startswith("[") and line.endswith("]"):
                break
            try:
                key, value = line.split(":", 1)
                data_res[key] = value
            except ValueError:
                continue
        file_object.seek(pos)  # return file pointer to the previous line
        return data_res

    @staticmethod
    def parse_comma_separated_section(file_object: TextIO) -> List[List[str]]:
        data_res = []
        while 1:
            pos = file_object.tell()
            line = file_object.readline()
            if not line:
                break
            line = line.rstrip()
            if line.startswith("//") or line == "":
                continue
            if line.startswith("[") and line.endswith("]"):
                break
            try:
                values = line.split(",")
                data_res.append(values)
            except ValueError:
                continue
        file_object.seek(pos)  # return file pointer to the previous line
        return data_res

    @staticmethod
    def parse_events_section(file_object: TextIO) -> List[Event]:
        data = _SectionParser.parse_comma_separated_section(file_object)
        new_data = []
        for event in data:
            new_data.append(Event(type=event[0], start_time=int(event[1]), params=event[2:]))
        return new_data

    @staticmethod
    def parse_timing_section(file_object: TextIO) -> List[TimingPoint]:
        data = _SectionParser.parse_comma_separated_section(file_object)
        new_data = []
        for point in data:
            new_data.append(TimingPoint(time=int(point[0]), beat_length=float(point[1]), meter=int(point[2]),
                                        sample_set=int(point[3]), sample_index=int(point[4]), volume=int(point[5]),
                                        uninherited=bool(point[6]), effects=int(point[7])))
        return new_data

    @staticmethod
    def parse_section(section_name: str, file_object: TextIO):
        match section_name:
            case "General":
                return _SectionParser.parse_key_value_section(file_object)
            case "Editor":
                return _SectionParser.parse_key_value_section(file_object)
            case "Metadata":
                return _SectionParser.parse_key_value_section(file_object)
            case "Difficulty":
                return _SectionParser.parse_key_value_section(file_object)
            case "Events":
                return _SectionParser.parse_events_section(file_object)
            case "TimingPoints":
                return _SectionParser.parse_timing_section(file_object)
            case "Colours":
                return _SectionParser.parse_key_value_section(file_object)
            case "HitObjects":
                return _SectionParser.parse_comma_separated_section(file_object)
            case _:
                return {}


class BeatmapFileParser:
    """
    Class for parsing Beatmap files
    Parsing ONLY std game mode
    """

    @staticmethod
    def _parse_osu_file(filepath: pathlib.Path | str, included_sections: List[str] = None) -> Dict[str, Any] | None:
        """
        Parsing .osu file into dictionary
        Parsing ONLY std game mode

        :param included_sections: Sections that function will parse
        :type: List[str]
        :param filepath: Path to the .osu file
        :type filepath: str
        :returns: dictionary of [section][key]: [value] pairs
        :rtype: dict
        :raises: FileExistsError: If file does not exist
        :raises: OSError
        """
        included_sections = set(included_sections)
        if included_sections is None:
            return None
        data = {}
        try:
            if isinstance(filepath, str):
                filepath = pathlib.Path(filepath)

            with open(filepath, "r", encoding='utf-8') as file:
                while 1:
                    line = file.readline()
                    if not line:
                        break
                    line = line.rstrip()
                    if line.startswith("[") and line.endswith("]"):
                        section_name = line[1:-1]
                        if section_name in included_sections:
                            data[section_name] = _SectionParser.parse_section(section_name, file)
                            if section_name == "General" and int(data[section_name]["Mode"]) != OSU_GAMEMODE_VALUE:
                                return None
                            included_sections.remove(section_name)
                            if not included_sections:
                                return data
                        elif section_name == "General":
                            temp_data = _SectionParser.parse_section(section_name, file)
                            if int(temp_data["Mode"]) != OSU_GAMEMODE_VALUE:
                                return None
                        else:
                            continue
        except FileExistsError:
            exc_msg = "File does not exists"
            logger.exception(exc_msg)
            raise FileExistsError(exc_msg)
        except OSError:
            exc_msg = "OS Error"
            logger.exception(exc_msg)
            raise OSError(exc_msg)

        return data

    @staticmethod
    def parse_osu_file_metadata(filepath: pathlib.Path | str):
        if isinstance(filepath, str):
            filepath = pathlib.Path(filepath)
        return BeatmapFileParser._parse_osu_file(filepath, included_sections=["Metadata"])

    @staticmethod
    def parse_full_osu_file(filepath: pathlib.Path | str):
        if isinstance(filepath, str):
            filepath = pathlib.Path(filepath)
        return BeatmapFileParser._parse_osu_file(filepath, included_sections=ALL_SECTION_NAMES)
