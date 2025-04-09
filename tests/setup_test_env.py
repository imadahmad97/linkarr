import os


class SetupTestEnv:
    def __init__(self):
        self.create_test_directory()
        self.setup_env_for_test_create_file_hardlink_01()
        self.setup_env_for_test_create_directory_hardlink_01()
        self.setup_env_for_test_hardlink_files_and_directories_01()

    @staticmethod
    def create_test_directory():
        """
        Create the test directory structure.
        """
        os.makedirs("tests/test_directory", exist_ok=True)

    @staticmethod
    def setup_env_for_test_create_file_hardlink_01():
        os.makedirs(
            "tests/test_directory/create_file_hardlink_01/source_dir", exist_ok=True
        )
        os.makedirs(
            "tests/test_directory/create_file_hardlink_01/target_dir", exist_ok=True
        )
        with open(
            "tests/test_directory/create_file_hardlink_01/source_dir/test_file.txt",
            "w",
        ) as f:
            f.write("This is a test file.")

    @staticmethod
    def setup_env_for_test_create_directory_hardlink_01():
        os.makedirs(
            "tests/test_directory/create_directory_hardlink_01/source_dir",
            exist_ok=True,
        )
        with open(
            "tests/test_directory/create_directory_hardlink_01/source_dir/test_file.txt",
            "w",
        ) as f:
            f.write("This is a test file.")

    @staticmethod
    def setup_env_for_test_hardlink_files_and_directories_01():
        os.makedirs(
            "tests/test_directory/hardlink_files_and_directories_01/source_dir",
            exist_ok=True,
        )
        os.makedirs(
            "tests/test_directory/hardlink_files_and_directories_01/source_dir/test_subdir",
            exist_ok=True,
        )
        os.makedirs(
            "tests/test_directory/hardlink_files_and_directories_01/target_dir",
            exist_ok=True,
        )
        with open(
            "tests/test_directory/hardlink_files_and_directories_01/source_dir/test_file.txt",
            "w",
        ) as f:
            f.write("This is a test file.")

        with open(
            "tests/test_directory/hardlink_files_and_directories_01/source_dir/test_subdir/test_file.txt",
            "w",
        ) as f:
            f.write("This is a test file 2.")
