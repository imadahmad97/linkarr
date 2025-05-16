from app.service.item_list_building_service import get_items_in_source_dir


def test_get_items_in_source_dir():
    items = get_items_in_source_dir(
        "tests/test_directory/get_items_in_source_dir_01/source_dir"
    )
    assert items == ["test_file.txt", "test_file_2.txt", "test_file_3.txt"]
