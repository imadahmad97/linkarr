from flask import render_template, request
from .config import Config


def init_routes(app):

    @app.route("/", methods=["GET", "POST"])
    def base():
        if request.method == "POST":
            uploaded_file = request.files.get("source")

        return render_template("base.html")
