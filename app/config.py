import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '7fb1a5uk'
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_HOST = os.environ['DB_HOST']
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://"+DB_USER+":"+DB_PASS+"@"+DB_HOST+"/"+DB_NAME\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

