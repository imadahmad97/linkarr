import os
from flask import flash, current_app as app
from app.model.config import Config
from app.model.user_selection import UserSelection


class UserSelectionValidator:
    def __init__(self, selection: UserSelection):
        self.selection = selection

    def validate_directories(self):
        self._check_selected()
        self._check_existence()
        self._check_in_config()

    def validate_items(self):
        self._check_items_selected()
        self._check_items_exist()

    def _check_selected(self):
        if not self.selection.selected_source_dir:
            app.logger.error("No source directory selected")
            flash("Please select a source directory.", "error")

        if not self.selection.selected_target_dir:
            app.logger.error("No target directory selected")
            flash("Please select a target directory.", "error")

    def _check_existence(self):
        if not os.path.exists(self.selection.selected_source_dir):
            app.logger.error(
                f"Source directory '{self.selection.selected_source_dir}' not found"
            )
            flash(
                f"Source directory '{self.selection.selected_source_dir}' not found.",
                "error",
            )

        if not os.path.exists(self.selection.selected_target_dir):
            app.logger.error(
                f"Target directory '{self.selection.selected_target_dir}' not found"
            )
            flash(
                f"Target directory '{self.selection.selected_target_dir}' not found.",
                "error",
            )

    def _check_in_config(self):
        if self.selection.selected_source_dir not in Config.source_dirs:
            app.logger.error("Source directory not in config")
            flash("Source directory not in config.", "error")

        if self.selection.selected_target_dir not in Config.target_dirs:
            app.logger.error("Target directory not in config")
            flash("Target directory not in config.", "error")

    def _check_items_selected(self):
        if not self.selection.selected_items:
            app.logger.error("No items selected")
            flash("Please select at least one item.", "error")

    def _check_items_exist(self):
        for item in self.selection.selected_items or []:
            path = os.path.join(self.selection.selected_source_dir, item)
            if not os.path.exists(path):
                app.logger.error(f"Item '{item}' not found")
                flash(f"Item '{item}' not found.", "error")
