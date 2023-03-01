import os

basedir = os.path.abspath(os.path.dirname(__file__))


# SQL-Alchemy config
class Config:
    db_name = 'app.db'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_name}.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
