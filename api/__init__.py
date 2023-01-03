from flask import Flask
import os
from .Config import Config

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # Loading configuration from Config.py (if it exists)
    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)

    # Importing Blueprints, CORS, and Flask_Mail
    from .api_routes import api_bp, cors, mail

    # Initializing cors
    cors.init_app(app, resources={r"/api/message": {"origins": app.config['CORS_ORIGIN']}})

    # Initializing Flask_Mail
    mail.init_app(app)

    # Registering Blueprints
    app.register_blueprint(api_bp)

    return app