from app.model.config import Config
from app.utils import clean_source_and_target_dir_names
from flask import current_app as app


def handle_post_request_for_config_page(
    source_dirs: list[str],
    target_dirs: list[str],
):

    # Step 1: Clean up the source_dirs and target_dirs lists
    app.logger.info("Cleaning up the source_dirs and target_dirs lists")
    cleaned_source_dirs, cleaned_target_dirs = clean_source_and_target_dir_names(
        source_dirs, target_dirs
    )

    # Step 2: Update the json data in the Config class
    app.logger.info("Updating the json data in the Config class")
    Config.update_json_data(cleaned_source_dirs, cleaned_target_dirs)

    # Step 3: Save the updated config data to the config.json file
    app.logger.info("Saving the updated config data to the config.json file")
    Config.save_json_data()

    # Step 4: Reload the Config class variables
    app.logger.info("Reloading the Config class variables")
    Config.reload_config_class_variables(cleaned_source_dirs, cleaned_target_dirs)
