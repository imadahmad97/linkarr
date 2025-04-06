from flask import request


def get_user_selection():
    selected_source_dir = request.form.get("selected_source_dir")
    selected_target_dir = request.form.get("selected_target_dir")
    selected_files = request.form.getlist("selected_files")

    return selected_source_dir, selected_target_dir, selected_files
