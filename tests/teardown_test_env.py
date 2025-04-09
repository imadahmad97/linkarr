import os
import shutil


def teardown_test_env():
    """
    Clean up the test environment by removing test directories and files.
    """
    # Remove the test directory if it exists
    test_dir = "tests/test_directory"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)


teardown_test_env()
