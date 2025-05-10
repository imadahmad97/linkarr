import os
from flask import current_app as app


def create_file_or_directory_symlink(source_file, target_dir):
    target_file = os.path.join(target_dir, os.path.basename(source_file))
    app.logger.info(f"Creating symbolic link for file: {source_file} -> {target_file}")
    if not os.path.islink(target_file):
        app.logger.info(f"This is happening")
        os.symlink(source_file, target_file)


def symbolically_link_files_and_directories(source_dir, target_dir, items):
    app.logger.info(f"Creating symbolic links for items: {items}")

    for item in items:
        app.logger.info(f"Processing item: {item}")
        item = os.path.basename(item)
        source = os.path.join(source_dir, item)

        create_file_or_directory_symlink(source, target_dir)
        app.logger.info(f"Successfully created symbolic link: {source} in {target_dir}")
