from flask import Flask

def create_app():
    app = Flask(__name__)
    # Registering blueprints
    from .views import main
    app.register_blueprint(main)

    return app

