from app.extensions import db

class JobStatusChange(db.Model):
    __tablename__ = 'job_status_change'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
