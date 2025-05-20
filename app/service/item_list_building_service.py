import os
from flask import current_app as app


def get_items_in_source_dir(source_dir):
    items = os.listdir(source_dir)
    items = sorted(items)
    return items


def build_items_and_links_dict(items, target_dir):
    app.logger.info("Building items and links dictionary")
    items_and_links = []
    for item in items:
        app.logger.info(f"Processing item: {item}")
        item_path = os.path.join(target_dir, item)
        if os.path.exists(item_path) or os.path.islink(item_path):
            app.logger.info(f"Item exists or is a link: {item_path}")
            item_dict = {}
            item_dict["name"] = item

            stat_info = os.lstat(item_path)

            if stat_info.st_nlink > 1 and not os.path.islink(item_path):
                app.logger.info(f"Item is a hardlink: {item_path}")
                item_dict["hardlink_status"] = True
            else:
                app.logger.info(f"Item is not a hardlink: {item_path}")
                item_dict["hardlink_status"] = False

            if os.path.islink(item_path):
                app.logger.info(f"Item is a symbolic link: {item_path}")
                item_dict["symbolic_link_status"] = True
            else:
                app.logger.info(f"Item is not a symbolic link: {item_path}")
                item_dict["symbolic_link_status"] = False

            items_and_links.append(item_dict)

        else:
            app.logger.info(f"Item does not exist or is not a link: {item_path}")
            item_dict = {}
            item_dict["name"] = item
            item_dict["hardlink_status"] = False
            item_dict["symbolic_link_status"] = False
            items_and_links.append(item_dict)

    app.logger.info("Finished building items and links dictionary")
    return items_and_links
