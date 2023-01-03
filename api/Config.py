from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    DEBUG = os.getenv("DEBUG")
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEVELOPMENT = os.getenv("DEVELOPMENT")
    API_KEY = os.getenv("API_KEY")
    CORS_ORIGIN = os.getenv("CORS_ORIGIN")
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USE_SSL = os.getenv("MAIL_USE_SSL")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEBUG = os.getenv("MAIL_DEBUG")