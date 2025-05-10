import os
from flask import current_app as app


def create_file_hardlink(source_file, target_dir):
    target_file = os.path.join(target_dir, os.path.basename(source_file))
    app.logger.debug(f"Creating hardlink for file: {source_file} -> {target_file}")
    if not os.path.exists(target_file):
        os.link(source_file, target_file)


def create_directory_hardlink(source_dir, target_dir):
    target_subdir = os.path.join(target_dir, os.path.basename(source_dir))
    os.makedirs(target_subdir, exist_ok=True)
    for root, dirs, files in os.walk(source_dir):
        relative_path = os.path.relpath(root, source_dir)
        target_root = os.path.join(target_subdir, relative_path)
        os.makedirs(target_root, exist_ok=True)
        for file in files:
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_root, file)
            if not os.path.exists(target_file):
                os.link(source_file, target_file)


def hardlink_files_and_directories(source_dir, target_dir, items):
    app.logger.info(f"Creating hardlinks for items: {items}")

    for item in items:
        app.logger.debug(f"Processing item: {item}")
        item = os.path.basename(item)
        source = os.path.join(source_dir, item)

        if os.path.isfile(source):
            app.logger.debug("File detected, creating hardlink")
            create_file_hardlink(source, target_dir)
        elif os.path.isdir(source):
            app.logger.debug("Directory detected, creating hardlink")
            create_directory_hardlink(source, target_dir)
