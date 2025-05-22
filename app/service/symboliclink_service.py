import os
from flask import current_app as app
from flask import flash


def create_file_or_directory_symlink(source_file, target_dir):
    target_file = os.path.join(target_dir, os.path.basename(source_file))
    app.logger.info(f"Creating symbolic link for file: {source_file} -> {target_file}")
    if os.path.islink(target_file):
        flash(f"Item {target_file} already symlinked!", "warning")
        app.logger.info(f"Item {target_file} already symlinked!")
    elif os.path.exists(target_file):
        flash(f"Item {target_file} already hardlinked!", "warning")
        app.logger.info(f"Item {target_file} already hardlinked!")
    else:
        os.symlink(source_file, target_file)
        flash(f"Item {target_file} symlinked!", "success")
        app.logger.info(f"Symbolic link created: {source_file} -> {target_file}")


def symbolically_link_files_and_directories(source_dir, target_dir, items):
    app.logger.info(f"Creating symbolic links for items: {items}")

    for item in items:
        app.logger.info(f"Processing item: {item}")
        item = os.path.basename(item)
        source = os.path.join(source_dir, item)

        create_file_or_directory_symlink(source, target_dir)
        app.logger.info(f"Successfully created symbolic link: {source} in {target_dir}")
