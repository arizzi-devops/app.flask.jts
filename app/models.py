from app import db

# Job model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    login = db.Column(db.String(12), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
