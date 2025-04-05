from app.utils_change import get_user_selection
from app.model.userselection import UserSelection


def handle_hardlink_submission():

    # Step 1: Get user selection and build UserSelection object
    selected_source_dir, selected_target_dir, selected_files = get_user_selection()

    user_selection = UserSelection(
        selected_source_dir, selected_target_dir, selected_files
    )

    # Step 2: Validate user selection
    user_selection.validate_user_selection()

    hardlink_files_and_directories(
        selected_source_dir, selected_target_dir, selected_files
    )
