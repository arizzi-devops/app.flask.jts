from app.extensions import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column()
    company = db.Column()
    url = db.Column()
    user_id = db.Column(db.Integer)
    salary_expectation = db.Column(db.Integer)
    location = db.Column(db.Integer)

    def __repr__(self):
        return f'<Job "{self.title}">'
