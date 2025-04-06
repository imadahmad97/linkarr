import os
from app.config import Config
from flask import request


class UserSelection:
    def __init__(self, selected_source_dir, selected_target_dir, selected_items):
        self.selected_source_dir = selected_source_dir
        self.selected_target_dir = selected_target_dir
        self.selected_items = selected_items

    @classmethod
    def build_user_selection_from_request(cls):
        selected_source_dir = request.form.get("selected_source_dir")
        selected_target_dir = request.form.get("selected_target_dir")
        selected_items = request.form.getlist("selected_items")

        return cls(selected_source_dir, selected_target_dir, selected_items)

    def validate_directories_and_items_are_selected(self):
        if not self.selected_source_dir:
            raise ValueError("Source directory not selected")
        if not self.selected_target_dir:
            raise ValueError("Target directory not selected")
        if not self.selected_items:
            raise ValueError("No items selected")

    def validate_directories_and_items_exist(self):
        if not os.path.exists(self.selected_source_dir):
            raise ValueError(f"Source directory '{self.selected_source_dir}' not found")
        if not os.path.exists(self.selected_target_dir):
            raise ValueError(f"Target directory '{self.selected_target_dir}' not found")
        for item in self.selected_items:
            item_path = os.path.join(self.selected_source_dir, item)
            if not os.path.exists(item_path):
                raise ValueError(f"Item '{item}' not found in source directory")

    def validate_directories_are_in_config(self):
        if self.selected_source_dir not in Config.source_dirs:
            raise ValueError("Invalid source directory selected")
        if self.selected_target_dir not in Config.target_dirs:
            raise ValueError("Invalid target directory selected")

    def validate_user_selection(self):
        try:
            self.validate_directories_and_items_are_selected()
            self.validate_directories_and_items_exist()
            self.validate_directories_are_in_config()
        except ValueError as e:
            raise e
