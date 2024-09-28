from flask import render_template, request, flash, redirect, url_for
from .config import Config
import os


def init_routes(app):

    @app.route("/", methods=["GET", "POST"])
    def base():
        if request.method == "POST":
            uploaded_file = request.files.get("source")
            if not uploaded_file:
                flash("No file uploaded", "error")
                return redirect(url_for("base"))

            # Construct the source file path
            source = os.path.join(Config.source_dir, uploaded_file.filename)

            # Check if source file exists
            if not os.path.exists(source):
                flash(f"Source file '{uploaded_file.filename}' not found", "error")
                return redirect(url_for("base"))

            # Check if target directory exists
            if not os.path.exists(Config.target_dir):
                flash(f"Target directory '{Config.target_dir}' not found", "error")
                return redirect(url_for("base"))

            # Proceed to create the hard link
            try:
                os.link(source, os.path.join(Config.target_dir, uploaded_file.filename))
                flash("File successfully linked", "success")
            except Exception as e:
                flash(f"Error linking file: {str(e)}", "error")

            return redirect(url_for("base"))

        return render_template("base.html")
