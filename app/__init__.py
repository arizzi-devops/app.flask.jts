from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SuP3rSecr3t!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@db/flask_app_db'
db = SQLAlchemy(app)

from app import routes
