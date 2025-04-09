from app.service.linking_service import hardlink_files_and_directories
from flask import current_app as app
from app.model.userselection import UserSelection


def handle_post_request_for_file_selector(
    selected_source_dir, selected_target_dir, selected_items
):

    # Step 1: Build user selection from request
    app.logger.info("Building user selection from POST request")
    user_selection = UserSelection(
        selected_source_dir, selected_target_dir, selected_items
    )

    # Step 2: Validate user selection
    app.logger.info("Validating user selection")
    user_selection.validate_user_directory_selection()
    user_selection.validate_user_item_selection()

    # Step 3: Perform hardlinking
    app.logger.info("Performing hardlinking")
    hardlink_files_and_directories(
        user_selection.selected_source_dir,
        user_selection.selected_target_dir,
        user_selection.selected_items,
    )
