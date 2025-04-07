from app.model.userselection import UserSelection
from app.service.linking_service import HardLinker
from app.service.get_items_in_source_dir import get_items_in_source_dir
from flask import current_app as app


def handle_post_request(selected_source_dir, selected_target_dir, selected_items):

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
    HardLinker.hardlink_files_and_directories(
        user_selection.selected_source_dir,
        user_selection.selected_target_dir,
        user_selection.selected_items,
    )


def handle_get_request(selected_source_dir, selected_target_dir):

    # Step 1: Build user selection from request
    app.logger.info("Building user selection from GET request")
    user_selection = UserSelection(selected_source_dir, selected_target_dir)

    # Step 2: Validate user selection
    app.logger.info("Validating user selection")
    user_selection.validate_user_directory_selection()

    # Step 3: Get items in source directory
    app.logger.info("Getting items in source directory")
    items = get_items_in_source_dir(user_selection.selected_source_dir)

    # Step 4: Return items for rendering
    app.logger.info("Returning items for rendering")
    return items
