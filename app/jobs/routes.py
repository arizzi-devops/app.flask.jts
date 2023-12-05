from flask import render_template, request, redirect, url_for, flash, jsonify
from app.jobs import bp
from app.extensions import db
from app.models.job import Job
from app.models.job_status_change import JobStatusChange
from flask_login import current_user, login_required

statuses = ["New", "Applied", "H.R.", "Tech", "Finished"]

@bp.route('/')
@login_required
def index():
    jobs = Job.query.filter_by(user_id=current_user.id).all()
    print(len(jobs))
    return render_template('jobs/kanban.html', jobs=jobs, user=current_user, statuses=statuses)


@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        job = Job(
            name = request.form["name"],
            company = request.form["company"],
            url = request.form["url"],
            salary_expectation = request.form["salary_expectation"],
            location = request.form["location"],
            status_id = 0,
            user_id = current_user.id
        )
        db.session.add(job)
        db.session.commit()
        flash('job added successfully.', 'success')
        return redirect(url_for('jobs.index'))
    return render_template('jobs/form.html', job={}, user=current_user)


@bp.route('/edit/<int:job_id>', methods=['GET', 'POST'])
@login_required
def edit(job_id):
    job = {}
    if request.method == 'POST':
        job = Job.query.filter_by(id=job_id, user_id=current_user.id).first()
        job.name = request.form['name']
        job.company = request.form['company']
        job.url = request.form['url']
        job.salary_expectation = request.form['salary_expectation']
        job.location = request.form['location']
        db.session.commit()
        flash('job updated successfully.', 'success')
        return redirect(url_for('jobs.index'))
    else:
        job = Job.query.get(job_id)
    return render_template('jobs/form.html', job=job, user=current_user)


@bp.route('/edit/<int:job_id>/status', methods=['POST'])
@login_required
def edit_status(job_id):
    job = Job.query.filter_by(id=job_id, user_id=current_user.id).first()
    old_status_id = job.status_id
    new_status_id = request.json["new_status_id"]

    if old_status_id == new_status_id:
        return jsonify({'status': 'success', 'message': 'Job status unchanged'}), 200

    # Create a JobStatusChange record
    job_status_change = JobStatusChange(
        job_id=job.id,
        job_status_change_old=old_status_id,
        job_status_change_new=new_status_id
    )

    # Update the job status
    job.status_id = new_status_id

    # Commit changes to the database
    db.session.add(job_status_change)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Job status updated'}), 200


@bp.route('/delete/<int:job_id>', methods=['POST'])
@login_required
def delete(job_id):
    if request.method == 'POST':
        job = Job.query.filter_by(id=job_id, user_id=current_user.id).first()
        db.session.delete(job)
        db.session.commit()
        flash('job updated successfully.', 'success')
        return redirect(url_for('jobs.index'))
    else:
        job = Job.query.get(job_id)
    return render_template('jobs/form.html', job=job, user=current_user)
