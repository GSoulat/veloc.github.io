#!/usr/local/bin/python
# from dotenv import load_dotenv
import os

from flask import Flask

# load_dotenv(override=True)


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    # from . import models
    from .routes import home, info

    # blueprint for auth routes in our app
    app.register_blueprint(home.home)
    app.register_blueprint(info.info)

    return app


app = create_app()
