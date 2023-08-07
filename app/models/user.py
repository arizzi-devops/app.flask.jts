from app.extensions import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(primary_key=True)
    name = db.Column()
    login = db.Column()
    password  = db.Column()
    is_active = db.Column()

    def __repr__(self):
        return f'<User "{self.title}">'
