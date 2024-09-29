import os
import json


class Config:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CONFIG_FILE_PATH = os.path.join(BASE_DIR, "config", "config.json")

    try:
        with open(CONFIG_FILE_PATH, "r") as f:
            config_data = json.load(f)
    except FileNotFoundError:
        config_data = {"source_dirs": [], "target_dirs": []}
        with open(CONFIG_FILE_PATH, "w") as f:
            json.dump(config_data, f, indent=4)
    except json.JSONDecodeError:
        raise Exception(
            f"Error decoding JSON from configuration file at {CONFIG_FILE_PATH}"
        )

    # Load source_dirs and target_dirs from config_data
    source_dirs = config_data.get("source_dirs", [])
    target_dirs = config_data.get("target_dirs", [])
