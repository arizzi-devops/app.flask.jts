from flask import render_template, request, redirect, url_for, flash
from app.auth import bp
from app.extensions import db
from app.models.user import User

from flask_login import login_user, login_required, logout_user, current_user

@bp.route('/login')
def login():
    return render_template('auth/login.html', user=current_user)

@bp.route('/signin', methods=['POST'])
def signin():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        remember_me = False
        if "remember_me" in request.form and request.form['remember_me'] == 'on':
            remember_me = True
        user = User.query.filter_by(login=login, password=password).first()
        if user:
            flash('Signed in successfully!', 'success')
            login_user(user, remember=remember_me)
            return redirect(url_for('main.index'))
        else:
            flash('erro no login!', 'danger')
    return render_template('auth/login.html', user=current_user)

@bp.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for('main.index'))