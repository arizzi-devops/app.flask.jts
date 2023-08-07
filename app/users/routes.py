from flask import render_template, request, redirect, url_for, flash
from app.users import bp
from app.extensions import db
from app.models.user import User
from flask_login import current_user, login_required

@bp.route('/')
def index():
    users = User.query.all()
    return render_template('users/list.html', users=users, user=current_user)


@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        user = User.query.filter_by(login=request.form['login']).first()
        if user:
            flash('login already exists, try another', 'warning')
        else:
            user = User(
                name = request.form['name'],
                login = request.form['login'],
                password = request.form['password']
            )
            db.session.add(user)
            db.session.commit()
            flash('user added successfully.', 'success')
            return redirect(url_for('users.index'))
    return render_template('users/form.html', users={}, user=current_user)


@bp.route('/<int:user_id>/edit', methods=['GET', 'POST'])
def edit(user_id):
    if request.method == 'POST':
        user = User.query.filter_by(id=user_id).first()
        new_is_active = 0
        if "is_active" in request.form and request.form['is_active'] == 'on':
            new_is_active = 1

        user.is_active = new_is_active
        user.name = request.form['name']
        if request.form['password'] != '':
            user.password = request.form['password']
        db.session.commit()
        flash('user updated successfully.', 'success')
        return redirect(url_for('users.index'))
    else:
        user = User.query.get(user_id)
    return render_template('users/form.html', users=user, user=current_user)

@bp.route('/<int:user_id>/delete', methods=['GET', 'POST'])
def delete(user_id):
    if request.method == 'POST':
        user = User.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
        flash('user deleted successfully.', 'success')
        return redirect(url_for('users.index'))
