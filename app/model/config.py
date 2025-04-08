import os
import json


class Config:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    CONFIG_FILE_PATH = os.path.join(BASE_DIR, "config", "config.json")

    source_dirs: list[str] = []
    target_dirs: list[str] = []
    config_data: dict = {}

    @classmethod
    def load_config_from_json(cls):
        with open(cls.CONFIG_FILE_PATH, "r") as f:
            cls.config_data = json.load(f)

        cls.source_dirs = cls.config_data.get("source_dirs", [])
        cls.target_dirs = cls.config_data.get("target_dirs", [])

    @classmethod
    def update_json_data(cls, source_dirs: list[str], target_dirs: list[str]):
        cls.config_data["source_dirs"] = source_dirs
        cls.config_data["target_dirs"] = target_dirs

    @classmethod
    def save_json_data(cls):
        with open(cls.CONFIG_FILE_PATH, "w") as f:
            json.dump(cls.config_data, f, indent=4)

    @classmethod
    def reload_config_class_variables(
        cls, source_dirs: list[str], target_dirs: list[str]
    ):
        cls.source_dirs = source_dirs
        cls.target_dirs = target_dirs
