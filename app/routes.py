from flask import render_template, request
from .config import Config


def init_routes(app):

    @app.route("/")
    def base():
        if request.method == "POST":
            print(request.form.get("source"))
            print(request.form.get("target"))
        return render_template("base.html")
