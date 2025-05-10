from app.service.hardlink_service import (
    create_file_hardlink,
    create_directory_hardlink,
    hardlink_files_and_directories,
)
import os
from app import create_app

app = create_app()
app.app_context().push()


def test_create_file_hardlink_01():
    source_file = (
        "tests/test_directory/create_file_hardlink_01/source_dir/test_file.txt"
    )
    target_dir = "tests/test_directory/create_file_hardlink_01/target_dir"
    create_file_hardlink(source_file, target_dir)
    target_file = (
        "tests/test_directory/create_file_hardlink_01/target_dir/test_file.txt"
    )
    assert os.path.exists(target_file)
    assert os.stat(target_file).st_nlink > 1
    assert os.path.samefile(source_file, target_file)


def test_create_directory_hardlink_01():
    source_dir = "tests/test_directory/create_directory_hardlink_01/source_dir"
    source_file = os.path.join(source_dir, "test_file.txt")
    target_dir = "tests/test_directory/create_directory_hardlink_01/target_dir"
    target_file = "tests/test_directory/create_directory_hardlink_01/target_dir/source_dir/test_file.txt"
    create_directory_hardlink(source_dir, target_dir)
    assert os.path.exists(target_file)
    assert os.stat(target_file).st_nlink > 1
    assert os.path.samefile(source_file, target_file)
    assert os.path.exists(target_dir)
    assert os.path.isdir(target_dir)


def test_hardlink_files_and_directories_01():
    source_dir = "tests/test_directory/hardlink_files_and_directories_01/source_dir"
    source_subdir = (
        "tests/test_directory/hardlink_files_and_directories_01/source_dir/test_subdir"
    )
    source_file = "tests/test_directory/hardlink_files_and_directories_01/source_dir/test_file.txt"
    source_subdir_file = "tests/test_directory/hardlink_files_and_directories_01/source_dir/test_subdir/test_file.txt"
    target_dir = "tests/test_directory/hardlink_files_and_directories_01/target_dir"
    target_file = "tests/test_directory/hardlink_files_and_directories_01/target_dir/test_file.txt"
    target_subdir_file = "tests/test_directory/hardlink_files_and_directories_01/target_dir/test_subdir/test_file.txt"
    items = [source_file, source_subdir]
    hardlink_files_and_directories(source_dir, target_dir, items)
    assert os.path.exists(target_file)
    assert os.stat(target_file).st_nlink > 1
    assert os.path.samefile(source_file, target_file)
    assert os.path.exists(target_subdir_file)
    assert os.stat(target_subdir_file).st_nlink > 1
    assert os.path.samefile(source_subdir_file, target_subdir_file)
    with open(
        "tests/test_directory/hardlink_files_and_directories_01/target_dir/test_file.txt",
        "r",
    ) as f:
        content = f.read()
        assert content == "This is a test file."
    assert os.path.exists(target_dir)
    assert os.path.isdir(target_dir)
    assert os.path.exists(source_dir)
    assert os.path.isdir(source_dir)
    assert os.path.exists(source_subdir)
    assert os.path.isdir(source_subdir)
    assert os.path.exists(source_file)
    assert os.path.isfile(source_file)
    assert os.path.exists(source_subdir_file)
    assert os.path.isfile(source_subdir_file)
    with open(
        "tests/test_directory/hardlink_files_and_directories_01/target_dir/test_subdir/test_file.txt",
        "r",
    ) as f:
        content = f.read()
        assert content == "This is a test file 2."
