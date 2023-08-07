from flask import render_template, request, redirect, url_for, flash
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


# @bp.route('/<int:user_id>/edit', methods=['GET', 'POST'])
# @login_required
# def edit(user_id):
#     if request.method == 'POST':
#         user = Job.query.filter_by(id=user_id).first()
#         new_is_active = 0
#         if "is_active" in request.form and request.form['is_active'] == 'on':
#             new_is_active = 1
# 
#         user.is_active = new_is_active
#         user.name = request.form['name']
#         if request.form['password'] != '':
#             user.password = request.form['password']
#         db.session.commit()
#         flash('user updated successfully.', 'success')
#         return redirect(url_for('users.index'))
#     else:
#         user = Job.query.get(user_id)
#     return render_template('users/form.html', users=user, user=current_user)
# 
# @bp.route('/<int:user_id>/delete', methods=['GET', 'POST'])
# @login_required
# def delete(user_id):
#     if request.method == 'POST':
#         user = Job.query.filter_by(id=user_id).first()
#         db.session.delete(user)
#         db.session.commit()
#         flash('user deleted successfully.', 'success')
#         return redirect(url_for('users.index'))
