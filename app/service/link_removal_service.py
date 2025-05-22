import os
import shutil
from flask import current_app as app


def remove_links(target_dir: str, items: list[str]) -> None:
    for item in items:
        app.logger.info(f"Processing item: {item}")
        item = os.path.basename(item)
        item_path = os.path.join(target_dir, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
            app.logger.info(f"Removed directory: {item_path}")
        elif os.path.islink(item_path) or os.path.isfile(item_path):
            os.remove(item_path)
            app.logger.info(f"Removed link: {item_path}")
        else:
            app.logger.warning(f"Item is neither a directory nor a link: {item_path}")
