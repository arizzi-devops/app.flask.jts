from flask import Flask

from app.config import Config
from app.extensions import db

from flask_login import LoginManager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.jobs import bp as jobs_bp
    app.register_blueprint(jobs_bp, url_prefix='/jobs')

    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    return app

