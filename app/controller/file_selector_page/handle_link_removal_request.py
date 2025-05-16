from flask import current_app as app
import os


def handle_link_removal_request(
    selected_target_dir: str,
    selected_items: list[str],
) -> None:
    app.logger.info("Handling link removal request")

    app.logger.info("Removing links")
    for item in selected_items:
        app.logger.info(f"Processing item: {item}")
        item = os.path.basename(item)
        target = os.path.join(selected_target_dir, item)

        os.remove(target)
        app.logger.info(f"Removed link: {target}")
    app.logger.info("Link removal request handled successfully")
