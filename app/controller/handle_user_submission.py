from app.model.userselection import UserSelection
from app.service.linking_service import HardLinker
from app.service.validation_service import ValidateUserSelection
from flask import current_app as app


def handle_user_submission():

    # Step 1: Build user selection from request
    app.logger.info("Building user selection from request")
    user_selection = UserSelection.build_user_selection_from_request()

    # Step 2: Validate user selection
    app.logger.info("Validating user selection")
    validator = ValidateUserSelection(user_selection)
    validator.validate_user_selection()

    # Step 3: Perform hardlinking
    app.logger.info("Performing hardlinking")
    HardLinker.hardlink_files_and_directories(
        user_selection.selected_source_dir,
        user_selection.selected_target_dir,
        user_selection.selected_items,
    )
