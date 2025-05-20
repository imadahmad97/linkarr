from flask import current_app as app
from app.model.userselection import UserSelection
from app.service.hardlink_service import hardlink_files_and_directories


def handle_hardlink_request(request):
    # Step 1: Extract the form data from the request
    selected_source_dir = request.form.get("selected_source_dir")
    app.logger.info(f"Selected source dir: {selected_source_dir}")

    selected_target_dir = request.form.get("selected_target_dir")
    app.logger.info(f"Selected target dir: {selected_target_dir}")

    selected_items = request.form.getlist("selected_items")
    app.logger.info(f"Selected items: {selected_items}")

    # Step 2: Build user selection from request
    app.logger.info("Building user selection from POST request")
    user_selection = UserSelection(
        selected_source_dir, selected_target_dir, "hard", selected_items
    )
    app.logger.info("Successfully built user selection")

    # Step 3: Validate user selection
    app.logger.info("Validating user selection")
    user_selection.validate_user_directory_selection()
    user_selection.validate_user_item_selection()
    app.logger.info("User selection validated successfully")

    # Step 4: Perform hardlinking
    app.logger.info("Performing hardlinking")
    hardlink_files_and_directories(
        user_selection.selected_source_dir,
        user_selection.selected_target_dir,
        user_selection.selected_items,
    )
    app.logger.info("Hardlinking completed successfully")

    # Step 5: Return user selection
    return user_selection
