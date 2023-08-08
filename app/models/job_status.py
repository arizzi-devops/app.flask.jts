from app.extensions import db

class JobStatus(db.Model):
    __tablename__ = 'job_status'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
