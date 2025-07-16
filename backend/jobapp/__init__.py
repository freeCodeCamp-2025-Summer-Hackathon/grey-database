import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from mongoengine import connect
from flasgger import Swagger

from jobapp.config import Config

# load environment variables
load_dotenv()

def create_app():

    # create app instance
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config())

    connect(host = app.config['MONGODB_SETTINGS'].get('host'))

    # Initialize Swagger
    if os.getenv("FLASK_ENV") == 'dev':
        Swagger(app)

    # cors
    CORS(app)

    from .API import main
    from .API import auth

    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp, url_prefix="/auth")
    return app
