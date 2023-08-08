from app.extensions import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column()
    location = db.Column()
    url = db.Column()
    status_id = db.Column()

    def __repr__(self):
        return f'<Job "{self.title}">'
