import os
from app.config import Config


class ValidateUserSelection:
    def __init__(self, user_selection):
        self.user_selection = user_selection

    def validate_directories_and_items_are_selected(self):
        if not self.user_selection.selected_source_dir:
            raise ValueError("Source directory not selected")
        if not self.user_selection.selected_target_dir:
            raise ValueError("Target directory not selected")
        if not self.user_selection.selected_items:
            raise ValueError("No items selected")

    def validate_directories_and_items_exist(self):
        if not os.path.exists(self.user_selection.selected_source_dir):
            raise ValueError(f"Source directory '{self.selected_source_dir}' not found")
        if not os.path.exists(self.user_selection.selected_target_dir):
            raise ValueError(f"Target directory '{self.selected_target_dir}' not found")
        for item in self.user_selection.selected_items:
            item_path = os.path.join(self.user_selection.selected_source_dir, item)
            if not os.path.exists(item_path):
                raise ValueError(f"Item '{item}' not found in source directory")

    def validate_directories_are_in_config(self):
        if self.user_selection.selected_source_dir not in Config.source_dirs:
            raise ValueError("Invalid source directory selected")
        if self.user_selection.selected_target_dir not in Config.target_dirs:
            raise ValueError("Invalid target directory selected")

    def validate_user_selection(self):
        try:
            self.validate_directories_and_items_are_selected()
            self.validate_directories_and_items_exist()
            self.validate_directories_are_in_config()
        except ValueError as e:
            raise e
