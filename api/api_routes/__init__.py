from flask import current_app
from .routes import api_bp, mail
from flask_cors import CORS

cors = CORS()