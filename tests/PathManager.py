import pathlib


class PathManager:
    PROJECT_ROOT: pathlib.Path = pathlib.Path(__file__).parent.parent

    @classmethod
    def set_project_root(cls, path: pathlib.Path):
        cls.PROJECT_ROOT = path
