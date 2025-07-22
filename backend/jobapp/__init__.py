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
    from .API import application
    from .API import note
    from .API import contact
    from .API import followup

    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp, url_prefix="/auth")
    app.register_blueprint(application.bp, url_prefix="/application")
    app.register_blueprint(note.bp, url_prefix='/application')
    app.register_blueprint(contact.bp, url_prefix='/applications')
    # app.register_blueprint(followup.bp, url_prefix='/applications')

    return app
