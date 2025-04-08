def clean_source_and_target_dir_names(
    source_dirs: list[str], target_dirs: list[str]
) -> tuple[list[str], list[str]]:
    source_dirs = [dir.strip() for dir in source_dirs if dir.strip()]
    target_dirs = [dir.strip() for dir in target_dirs if dir.strip()]

    return source_dirs, target_dirs
