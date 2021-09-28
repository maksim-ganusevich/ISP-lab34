from flask import Flask
from flask_restful import Api
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.restapi import *


restapi = Flask(__name__)
api = Api(restapi)
api.add_resource(RestApi, '/rest', '/rest/', '/rest/<string:id>', '/rest/<int:id>')
restapi.config.from_object(Config)
db = SQLAlchemy(restapi)
migrate = Migrate(restapi, db)


from app.database_models import *
