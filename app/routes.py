from flask import render_template, request, redirect, url_for, flash, Markup
from app.controller.file_selector_page.handle_post_request import (
    handle_link_request,
)
from app.controller.file_selector_page.handle_get_request import (
    handle_get_request_for_file_selector,
)
from app.controller.config_page.handle_post_request import (
    handle_post_request_for_config_page,
)
from app.controller.file_selector_page.handle_link_removal_request import (
    handle_link_removal_request,
)
from .model.config import Config
import logging
from app.controller.file_selector_page.handle_hardlink_request import (
    handle_hardlink_request,
)

logger = logging.getLogger(__name__)


def init_routes(app):

    @app.route("/", methods=["GET", "POST"])
    def base():
        if request.method == "POST":
            app.logger.info("Handling POST request for file selector")

            selected_source_dir = request.form.get("selected_source_dir")
            app.logger.info(f"Selected source dir: {selected_source_dir}")
            selected_target_dir = request.form.get("selected_target_dir")
            app.logger.info(f"Selected target dir: {selected_target_dir}")
            link_type = request.form.get("link_type")
            app.logger.info(f"Selected link type: {link_type}")
            selected_items = request.form.getlist("selected_items")
            app.logger.info(f"Selected items: {selected_items}")

            handle_link_request(
                selected_source_dir, selected_target_dir, link_type, selected_items
            )
            app.logger.info("Handling POST request completed, files linked")

            if link_type == "hard":
                for item in selected_items:
                    flash(
                        Markup(
                            f"Hardlinked&nbsp;<strong>{item}</strong>&nbsp;from&nbsp;<strong>{selected_source_dir}</strong>&nbsp;to&nbsp;<strong>{selected_target_dir}</strong>&nbsp;\u2713"
                        )
                    )

            elif link_type == "symbolic":
                for item in selected_items:
                    flash(
                        Markup(
                            f"Symbolically Linked&nbsp;<strong>{item}</strong>&nbsp;from&nbsp;<strong>{selected_source_dir}</strong>&nbsp;to&nbsp;<strong>{selected_target_dir}</strong>&nbsp;\u2713"
                        )
                    )

            return redirect(
                url_for(
                    "base",
                    selected_source_dir=selected_source_dir,
                    selected_target_dir=selected_target_dir,
                )
            )

        elif request.method == "GET":
            app.logger.info("Handling GET request for file selector")

            selected_source_dir = request.args.get("selected_source_dir")
            app.logger.info(f"Selected source dir: {selected_source_dir}")
            selected_target_dir = request.args.get("selected_target_dir")
            app.logger.info(f"Selected target dir: {selected_target_dir}")
            items = []

            if selected_source_dir:
                app.logger.info("Getting items for rendering")
                items = handle_get_request_for_file_selector(
                    selected_source_dir, selected_target_dir
                )
                app.logger.info("Successfully retrieved items for rendering")

            return render_template(
                "file_selector.html",
                items=items,
                source_dirs=Config.source_dirs,
                target_dirs=Config.target_dirs,
                selected_source_dir=selected_source_dir,
                selected_target_dir=selected_target_dir,
            )

    @app.route("/hardlink", methods=["POST"])
    def hardlink():
        app.logger.info("Handling POST request for file selector")

        user_selection = handle_hardlink_request(request)

        app.logger.info("Handling POST request completed, files linked")

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
