from app.extensions import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column()
    login = db.Column()
    password  = db.Column()
    is_active = db.Column(db.Boolean, unique=False, default=True)

    def __repr__(self):
        return f'<User "{self.title}">'
