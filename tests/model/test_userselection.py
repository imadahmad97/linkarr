from app.model.userselection import UserSelection
import pytest


def test_user_selection_init():
    selected_source_dir = "source_dir"
    selected_target_dir = "target_dir"
    selected_items = ["item1", "item2"]

    user_selection = UserSelection(
        selected_source_dir, selected_target_dir, selected_items
    )

    assert user_selection.selected_source_dir == selected_source_dir
    assert user_selection.selected_target_dir == selected_target_dir
    assert user_selection.selected_items == selected_items


def test_validate_directories_are_selected():
    selected_source_dir = "source_dir"
    selected_target_dir = "target_dir"
    user_selection_both_selected = UserSelection(
        selected_source_dir, selected_target_dir
    )
    user_selection_no_source = UserSelection(None, selected_target_dir)
    user_selection_no_target = UserSelection(selected_source_dir, None)

    assert user_selection_both_selected.validate_directories_are_selected() is None
    with pytest.raises(ValueError) as excinfo:
        user_selection_no_source.validate_directories_are_selected()
        assert str(excinfo.value) == "Source directory not selected"
    with pytest.raises(ValueError) as excinfo:
        user_selection_no_target.validate_directories_are_selected()
        assert str(excinfo.value) == "Target directory not selected"


def test_validate_directories_exist():
    selected_source_dir = (
        "tests/test_directory/validate_directories_exist_01/source_dir"
    )
    selected_target_dir = (
        "tests/test_directory/validate_directories_exist_01/target_dir"
    )

    user_selection_both_exist = UserSelection(selected_source_dir, selected_target_dir)
    user_selection_source_not_exist = UserSelection(
        "non_existent_source", selected_target_dir
    )
    user_selection_target_not_exist = UserSelection(
        selected_source_dir, "non_existent_target"
    )

    assert user_selection_both_exist.validate_directories_exist() is None
    with pytest.raises(ValueError) as excinfo:
        user_selection_source_not_exist.validate_directories_exist()
        assert str(excinfo.value) == "Source directory 'non_existent_source' not found"
    with pytest.raises(ValueError) as excinfo:
        user_selection_target_not_exist.validate_directories_exist()
        assert str(excinfo.value) == "Target directory 'non_existent_target' not found"
