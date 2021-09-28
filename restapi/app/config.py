import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://qwerty:1234@localhost:5432/flask_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

