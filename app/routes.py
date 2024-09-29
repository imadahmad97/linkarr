from flask import render_template, request, flash, redirect, url_for
from .config import Config
import json
import os


def init_routes(app):

    @app.route("/", methods=["GET", "POST"])
    def base():
        if request.method == "POST":
            selected_source_dir = request.form.get("selected_source_dir")
            selected_target_dir = request.form.get("selected_target_dir")
            selected_items = request.form.getlist("selected_items")

            if not selected_items:
                flash("No items selected", "error")
                return redirect(url_for("base"))

            if not selected_source_dir or not selected_target_dir:
                flash("Source or target directory not selected", "error")
                return redirect(url_for("base"))

            # Validate the selected source and target directories
            if selected_source_dir not in Config.source_dirs:
                flash("Invalid source directory selected", "error")
                return redirect(url_for("base"))

            if selected_target_dir not in Config.target_dirs:
                flash("Invalid target directory selected", "error")
                return redirect(url_for("base"))

            if not os.path.exists(selected_target_dir):
                flash(f"Target directory '{selected_target_dir}' not found", "error")
                return redirect(url_for("base"))

            for item in selected_items:
                # Sanitize the item to prevent path traversal attacks
                item = os.path.basename(item)
                source = os.path.join(selected_source_dir, item)
                if not os.path.exists(source):
                    flash(f"Source '{item}' not found", "error")
                    continue

                try:
                    if os.path.isfile(source):
                        # If source is a file, create a hardlink in the target directory
                        target_file = os.path.join(
                            selected_target_dir, os.path.basename(source)
                        )
                        if not os.path.exists(target_file):
                            os.link(source, target_file)
                            flash(f"File '{item}' successfully linked", "success")
                        else:
                            flash(
                                f"File '{item}' already exists in target directory",
                                "warning",
                            )
                    elif os.path.isdir(source):
                        # If source is a directory
                        target_subdir = os.path.join(
                            selected_target_dir, os.path.basename(source)
                        )
                        if os.path.exists(target_subdir):
                            flash(
                                f"Directory '{item}' already exists in target directory",
                                "warning",
                            )
                        else:
                            os.makedirs(target_subdir, exist_ok=True)
                            flash(
                                f"Directory '{item}' created in target directory",
                                "success",
                            )
                        for root, dirs, files in os.walk(source):
                            # Recreate directory structure
                            relative_path = os.path.relpath(root, source)
                            target_root = os.path.join(target_subdir, relative_path)
                            os.makedirs(target_root, exist_ok=True)
                            for file in files:
                                source_file = os.path.join(root, file)
                                target_file = os.path.join(target_root, file)
                                if not os.path.exists(target_file):
                                    os.link(source_file, target_file)
                                    flash(
                                        f"File '{os.path.join(item, relative_path, file)}' successfully linked",
                                        "success",
                                    )
                                else:
                                    flash(
                                        f"File '{os.path.join(item, relative_path, file)}' already exists in target directory",
                                        "warning",
                                    )
                    else:
                        flash(
                            f"Source '{item}' is neither a file nor a directory",
                            "error",
                        )
                except Exception as e:
                    flash(f"Error linking '{item}': {str(e)}", "error")

            return redirect(url_for("base"))

        else:
            # GET request, display the source and target directory selection
            selected_source_dir = request.args.get("selected_source_dir")
            selected_target_dir = request.args.get("selected_target_dir")

            source_dirs = Config.source_dirs
            target_dirs = Config.target_dirs

            items = []
            if selected_source_dir:
                if selected_source_dir in source_dirs:
                    try:
                        items = os.listdir(selected_source_dir)
                        items = sorted(items)
                    except Exception as e:
                        flash(f"Error reading source directory: {str(e)}", "error")
                else:
                    flash("Invalid source directory selected", "error")

            return render_template(
                "file_selector.html",
                items=items,
                source_dirs=source_dirs,
                target_dirs=target_dirs,
                selected_source_dir=selected_source_dir,
                selected_target_dir=selected_target_dir,
            )

    @app.route("/config", methods=["GET", "POST"])
    def config():
        if request.method == "POST":
            # Get lists of directories from the form data
            source_dirs = request.form.getlist("source_dirs")
            target_dirs = request.form.getlist("target_dirs")

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
        return render_template("config.html", config=Config.config_data)
