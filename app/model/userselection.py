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
