from app.utils_change import get_user_selection
from app.model.userselection import UserSelection


def handle_user_submission():

    # Step 1: Get user selection and build UserSelection object from it
    user_selection = UserSelection(*get_user_selection())

    # Step 2: Validate user selection
    user_selection.validate_user_selection()

    hardlink_files_and_directories(
        selected_source_dir, selected_target_dir, selected_files
    )
