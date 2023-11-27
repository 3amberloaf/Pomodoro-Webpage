"""A simple flask web app"""
import flask_login
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect

import os
from flask import Flask
from app.context_processors import utility_text_processors
from app.simple_pages import simple_pages
from app.auth import auth
from app.exceptions import http_exceptions
from app.db.models import User
from app.db import db
from app.auth import auth
from app.cli import create_database


login_manager = flask_login.LoginManager()


def page_not_found(e):
    return render_template("404.html"), 404


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = 'This is an INSECURE secret!! DO NOT use this in production!!'
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    csrf = CSRFProtect(app)
    bootstrap = Bootstrap5(app)
    app.register_blueprint(simple_pages)
    app.register_blueprint(auth)
    app.context_processor(utility_text_processors)
    app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'Simplex'
    app.register_error_handler(404, page_not_found)
    # app.add_url_rule("/", endpoint="index")
    db_dir = "database/db.sqlite"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.abspath(db_dir)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    # add command function to cli commands
    app.cli.add_command(create_database)
    # Setup Flask-User and specify the User data-model

    return app


@login_manager.user_loader
def user_loader(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None
