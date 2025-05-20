from flask import current_app as app
import os
from app.model.user_selection import UserSelection
from app.model.user_selection_validator import UserSelectionValidator


def handle_link_removal_request(request) -> UserSelection:

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
        selected_source_dir, selected_target_dir, selected_items
    )

    # Step 3: Validate user selection
    app.logger.info("Validating user selection")
    validator = UserSelectionValidator(user_selection)
    app.logger.info("Validating directories")
    validator.validate_directories()
    app.logger.info("Validating items")
    validator.validate_items()

    app.logger.info("Validation completed successfully")
    # Step 2: Remove links
    app.logger.info("Removing links")
    for item in user_selection.selected_items:  # type: ignore
        app.logger.info(f"Processing item: {item}")
        item = os.path.basename(item)
        target = os.path.join(selected_target_dir, item)

        os.remove(target)
        app.logger.info(f"Removed link: {target}")

    app.logger.info("Link removal request handled successfully")

    # Step 3: Return user selection
    return user_selection
