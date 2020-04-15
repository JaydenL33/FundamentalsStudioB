from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch

cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    cors.init_app(app)

    from .routes import api
    app.register_blueprint(api)

    return app
