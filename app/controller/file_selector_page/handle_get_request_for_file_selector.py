from app.service.item_list_building_service import (
    get_items_in_source_dir,
    build_items_and_links_dict,
)
from app.model.user_selection import UserSelection
from app.model.user_selection_validator import UserSelectionValidator
from flask import current_app as app


def handle_get_request_for_file_selector(request):

    app.logger.info("Getting items for rendering")
    # Step 1: See if the user has provided a source directory
    if request.args.get("selected_source_dir"):
        # Step 2: Get selected source and target directories from request
        selected_source_dir = request.args.get("selected_source_dir")
        app.logger.info(f"Selected source dir: {selected_source_dir}")
        selected_target_dir = request.args.get("selected_target_dir")
        app.logger.info(f"Selected target dir: {selected_target_dir}")

        # Step 3: Build user selection from request
        app.logger.info("Building user selection from GET request")
        user_selection = UserSelection(selected_source_dir, selected_target_dir)

        # Step 3: Validate user selection
        app.logger.info("Validating user selection")
        validator = UserSelectionValidator(user_selection)
        app.logger.info("Validating directories")
        validator.validate_directories()

        app.logger.info("Validation completed successfully")
        # Step 5: Get list items in source directory
        app.logger.info("Getting items in source directory")
        items = get_items_in_source_dir(user_selection.selected_source_dir)

        # Step 6: Get items and links dictionary
        app.logger.info("Building items and links dictionary")
        items_with_links = build_items_and_links_dict(
            items, user_selection.selected_target_dir
        )

        # Step 7: Return items for rendering
        app.logger.info("Returning items for rendering")
        return user_selection, items_with_links

    # Step 8: If no source directory is provided, return empty user selection and items
    app.logger.info(
        "No source directory provided, returning empty user selection and items"
    )
    return UserSelection("", "", []), []
