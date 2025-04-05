def handle_hardlink_submission():
    selected_source_dir, selected_target_dir, selected_files = get_user_selection()

    validate_user_selection(selected_source_dir, selected_target_dir, selected_files)

    hardlink_files_and_directories(
        selected_source_dir, selected_target_dir, selected_files
    )
