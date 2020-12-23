from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#dk)(023_2hkj' # Secret Key Of the App

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    db.init_app(app) # Initiate a connection btn db and an app
    # Registering blueprints
    from .views import main
    app.register_blueprint(main)

    return app

