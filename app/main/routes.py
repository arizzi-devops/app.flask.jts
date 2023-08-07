from flask import render_template, flash
from app.main import bp
from flask_login import login_required, current_user

@bp.route('/')
def index():
    return render_template('index.html', user=current_user)
