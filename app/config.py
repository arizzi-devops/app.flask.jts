import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '7fb1a5uk'
    DB_HOST = 'db'
    DB_HOST = '192.168.127.132'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@'+ DB_HOST +'/flask_app_db'\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

