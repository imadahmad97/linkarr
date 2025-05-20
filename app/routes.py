import logging

from flask import redirect, render_template, request, url_for

from app.controller.config_page.handle_post_request import (
    handle_post_request_for_config_page,
)
from app.controller.file_selector_page.handle_get_request_for_file_selector import (
    handle_get_request_for_file_selector,
)
from app.controller.file_selector_page.handle_hardlink_request import (
    handle_hardlink_request,
)
from app.controller.file_selector_page.handle_link_removal_request import (
    handle_link_removal_request,
)
from app.controller.file_selector_page.handle_symlink_request import (
    handle_symlink_request,
)

from .model.config import Config

logger = logging.getLogger(__name__)


def init_routes(app):

    @app.route("/", methods=["GET", "POST"])
    def base():
        app.logger.info("Handling GET request for file selector")

        user_selection, items = handle_get_request_for_file_selector(request)

        app.logger.info("Handling GET request for file selector completed")

        return render_template(
            "file_selector.html",
            items=items,
            source_dirs=Config.source_dirs,
            target_dirs=Config.target_dirs,
            selected_source_dir=user_selection.selected_source_dir,
            selected_target_dir=user_selection.selected_target_dir,
        )

    @app.route("/hardlink", methods=["POST"])
    def hardlink():
        app.logger.info("Handling hardlink request for file selector")

        user_selection = handle_hardlink_request(request)

        app.logger.info("Handling hardlink request completed, files linked")

        return redirect(
            url_for(
                "base",
                selected_source_dir=user_selection.selected_source_dir,
                selected_target_dir=user_selection.selected_target_dir,
            )
        )

    @app.route("/symlink", methods=["POST"])
    def symlink():
        app.logger.info("Handling symlink request for file selector")

        user_selection = handle_symlink_request(request)

        app.logger.info("Handling symlink request completed, files linked")

        return redirect(
            url_for(
                "base",
                selected_source_dir=user_selection.selected_source_dir,
                selected_target_dir=user_selection.selected_target_dir,
            )
        )

    @app.route("/remove_link", methods=["POST"])
    def remove_link():
        app.logger.info("Handling POST request for remove link")
        selected_source_dir = request.form.get("selected_source_dir")
        app.logger.info(f"Selected source dir: {selected_source_dir}")
        selected_target_dir = request.form.get("selected_target_dir")
        app.logger.info(f"Selected target dir: {selected_target_dir}")
        selected_items = request.form.getlist("selected_items")
        app.logger.info(f"Selected items: {selected_items}")

        handle_link_removal_request(selected_target_dir, selected_items)
        app.logger.info("Handling POST request for remove link completed")
        return redirect(
            url_for(
                "base",
                selected_source_dir=selected_source_dir,
                selected_target_dir=selected_target_dir,
            )
        )

    @app.route("/config", methods=["GET", "POST"])
    def config():
        if request.method == "POST":
            # Get lists of directories from the form data
            app.logger.info("Handling POST request for config")

            source_dirs = request.form.getlist("source_dirs")
            app.logger.info(f"Source directories: {source_dirs}")
            target_dirs = request.form.getlist("target_dirs")
            app.logger.info(f"Target directories: {target_dirs}")

            handle_post_request_for_config_page(source_dirs, target_dirs)
            return redirect(url_for("config"))

        # GET request
        app.logger.info("Rendering config page")
        return render_template("config.html", config=Config.config_data)
