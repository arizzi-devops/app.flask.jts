from app.extensions import db
from app.models.job_status_change import JobStatusChange

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column()
    company = db.Column()
    url = db.Column()
    status_id = db.Column()
    user_id = db.Column(db.Integer)
    salary_expectation = db.Column(db.Integer)
    location = db.Column(db.Integer)
    is_archived = db.Column(db.Boolean, unique=False, default=False)

    def __repr__(self):
        return f'<Job "{self.name}">'

    def get_jobs_with_latest_update(user_id):
        subquery = db.session.query(
            JobStatusChange.job_id,
            db.func.max(JobStatusChange.change_timestamp).label('max_change_timestamp')
        ).group_by(JobStatusChange.job_id).subquery()

        query = db.session.query(
            Job.id,
            Job.status_id,
            Job.name,
            Job.company,
            subquery.c.max_change_timestamp.label('latest_update')
        ).outerjoin(subquery, Job.id == subquery.c.job_id).filter(Job.user_id == user_id)

        results = query.all()

        return results
