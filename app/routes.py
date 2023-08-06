from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User, Job

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        name = request.form['name']
        login = request.form['login']
        password = request.form['password']
        is_active = 0
        if request.form['is_active'] == 'active':
            is_active = 1
        new_user = User(name=name, login=login, password=password, is_active=is_active)
        db.session.add(new_user)
        db.session.commit()
    users = User.query.all()
    return render_template('user.html', users=users)

@app.route('/jobs', methods=['GET', 'POST'])
def jobs():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        url = request.form['url']
        new_job = Job(name=name, location=location, url=url)
        db.session.add(new_job)
        db.session.commit()
    jobs = Job.query.all()
    return render_template('job.html', jobs=jobs)

@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.login = request.form['login']
        user.password = request.form['password']
        user.is_active = 'is_active' in request.form
        db.session.commit()
        return redirect(url_for('users'))
    return render_template('edit_user.html', user=user)

@app.route('/edit_job/<int:job_id>', methods=['GET', 'POST'])
def edit_job(job_id):
    job = Job.query.get_or_404(job_id)
    if request.method == 'POST':
        job.name = request.form['name']
        job.location = request.form['location']
        job.url = request.form['url']
        db.session.commit()
        return redirect(url_for('jobs'))
    return render_template('edit_job.html', job=job)
