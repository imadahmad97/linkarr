import os


def get_items_in_source_dir(source_dir):
    items = os.listdir(source_dir)
    items = sorted(items)
    return items
