from flask import render_template, request, flash, redirect, url_for
from .config import Config
import os


def init_routes(app):

    @app.route("/", methods=["GET", "POST"])
    def base():
        if request.method == "POST":
            selected_items = request.form.getlist("selected_items")
            if not selected_items:
                flash("No items selected", "error")
                return redirect(url_for("file_selector"))

            # Check if target directory exists
            if not os.path.exists(Config.target_dir):
                flash(f"Target directory '{Config.target_dir}' not found", "error")
                return redirect(url_for("file_selector"))

            for item in selected_items:
                # Sanitize the item to prevent path traversal attacks
                item = os.path.basename(item)
                source = os.path.join(Config.source_dir, item)
                if not os.path.exists(source):
                    flash(f"Source '{item}' not found", "error")
                    continue

                try:
                    if os.path.isfile(source):
                        # If source is a file, create a hardlink in the target directory
                        target_file = os.path.join(
                            Config.target_dir, os.path.basename(source)
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
                            Config.target_dir, os.path.basename(source)
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

            return redirect(url_for("file_selector"))

        else:
            # GET request, list the items in source directory
            try:
                items = os.listdir(Config.source_dir)
                items = sorted(items)
            except Exception as e:
                items = []
                flash(f"Error reading source directory: {str(e)}", "error")
            return render_template("file_selector.html", items=items)
