import os


class HardLinker:
    def create_file_hardlink(self, source_file, target_dir):
        target_file = os.path.join(target_dir, os.path.basename(source_file))
        if not os.path.exists(target_file):
            os.link(source_file, target_file)

    def create_directory_hardlink(self, source_dir, target_dir):
        target_subdir = os.path.join(target_dir, os.path.basename(source_dir))
        os.makedirs(target_subdir, exist_ok=True)
        for root, dirs, files in os.walk(source_dir):
            relative_path = os.path.relpath(root, source_dir)
            target_root = os.path.join(target_subdir, relative_path)
            os.makedirs(target_root, exist_ok=True)
            for file in files:
                source_file = os.path.join(root, file)
                target_file = os.path.join(target_root, file)
                if not os.path.exists(target_file):
                    os.link(source_file, target_file)
