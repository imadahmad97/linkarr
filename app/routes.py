from flask import render_template, request, flash, redirect, url_for
from app.controller.file_selector.handle_post_request import (
    handle_post_request_for_file_selector,
)
from app.controller.file_selector.handle_get_request import (
    handle_get_request_for_file_selector,
)
from .config import Config
import json
import logging

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
            selected_items = request.form.getlist("selected_items")
            app.logger.info(f"Selected items: {selected_items}")

            handle_post_request_for_file_selector(
                selected_source_dir, selected_target_dir, selected_items
            )
            app.logger.info("Handling POST request completed, files hardlinked")
            return redirect(url_for("base"))

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

    @app.route("/config", methods=["GET", "POST"])
    def config():
        if request.method == "POST":
            # Get lists of directories from the form data
            app.logger.info("Handling POST request for config")
            source_dirs = request.form.getlist("source_dirs")
            app.logger.info(f"Source directories: {source_dirs}")
            target_dirs = request.form.getlist("target_dirs")
            app.logger.info(f"Target directories: {target_dirs}")

            # Clean up directories (remove empty entries)
            source_dirs = [dir.strip() for dir in source_dirs if dir.strip()]
            target_dirs = [dir.strip() for dir in target_dirs if dir.strip()]

            # Update the config_data
            Config.config_data["source_dirs"] = source_dirs
            Config.config_data["target_dirs"] = target_dirs

            # Save the updated config_data back to the config.json file
            try:
                with open(Config.CONFIG_FILE_PATH, "w") as f:
                    json.dump(Config.config_data, f, indent=4)
                flash("Configuration updated successfully.", "success")

                # Reload configurations
                Config.source_dirs = source_dirs
                Config.target_dirs = target_dirs
            except Exception as e:
                flash(f"Error saving configuration: {str(e)}", "error")

            return redirect(url_for("config"))

        # GET request
        app.logger.info("Rendering config page")
        return render_template("config.html", config=Config.config_data)
