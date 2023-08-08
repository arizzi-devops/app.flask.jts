from flask import render_template, request, redirect, url_for, flash, jsonify
from app.jobs import bp
from app.extensions import db
from app.models.job import Job
from flask_login import current_user, login_required

statuses = ["New", "Applied", "H.R.", "Tech", "Finished"]

@bp.route('/')
@login_required
def index():
    jobs = Job.query.all()
    print(len(jobs))
    return render_template('jobs/kanban.html', jobs=jobs, user=current_user, statuses=statuses)


@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        job = Job(
            name = request.form["name"],
            location = request.form["location"],
            url = request.form["url"],
            status_id = 1
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
        job = Job.query.filter_by(id=job_id).first()
        job.name = request.form['name']
        job.location = request.form['location']
        job.url = request.form['url']
        db.session.commit()
        flash('job updated successfully.', 'success')
        return redirect(url_for('jobs.index'))
    else:
        job = Job.query.get(job_id)
    return render_template('jobs/form.html', job=job, user=current_user)


@bp.route('/edit/<int:job_id>/status', methods=['POST'])
@login_required
def edit_status(job_id):
    job = Job.query.filter_by(id=job_id).first()
    job.status_id = request.json["new_status_id"]
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Job status updated'}), 200


@bp.route('/delete/<int:job_id>', methods=['POST'])
@login_required
def delete(job_id):
    if request.method == 'POST':
        job = Job.query.filter_by(id=job_id).first()
        db.session.delete(job)
        db.session.commit()
        flash('job updated successfully.', 'success')
        return redirect(url_for('jobs.index'))
    else:
        job = Job.query.get(job_id)
    return render_template('jobs/form.html', job=job, user=current_user)