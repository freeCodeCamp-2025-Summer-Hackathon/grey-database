from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from mongoengine import connect
import os
from flasgger import Swagger

#load environment variables
load_dotenv()

def create_app():
    
    # create app instance
    app = Flask(__name__, instance_relative_config=True)
    
    # db connect
    mongodb_uri = os.getenv("MONGODB_URI")
    connect(host=mongodb_uri)

    # Initialize Swagger
    Swagger(app)

    # cors
    CORS(app)
    
    from .API import main
    from .API import userAuth
    app.register_blueprint(main.bp)
    app.register_blueprint(userAuth.bp)
    return app
