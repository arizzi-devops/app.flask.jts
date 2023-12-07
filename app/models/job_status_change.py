from app.extensions import db
import datetime

class JobStatusChange(db.Model):
    __tablename__ = 'job_status_change'
    
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer)
    change_timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    job_status_change_old = db.Column(db.Integer)
    job_status_change_new = db.Column(db.Integer)

    def __repr__(self):
        return f'<JobStatusChange "{self.title}">'
