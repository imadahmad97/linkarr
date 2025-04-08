from app.service.get_items_in_source_dir import get_items_in_source_dir
from app.model.userselection import UserSelection
from flask import current_app as app


def handle_get_request_for_file_selector(selected_source_dir, selected_target_dir):

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
