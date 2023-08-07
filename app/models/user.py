from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column()
    login = db.Column()
    password  = db.Column()
    is_active = db.Column(db.Boolean, unique=False, default=True)

    def __repr__(self):
        return f'<User "{self.title}">'
