from app.blueprints.admin import admin
from app.blueprints.auth import auth
from app.blueprints.errors import errors
from app.blueprints.home import home
from app.extensions import (
    bootstrap, csrf, db, login_manager, migrate)

FLASK_BLUEPRINTS = [admin, auth, home, errors]


def authentication(app, user_model):
    """
    Initialize the Flask-Login extension (mutates the app passed in).

    :param app: Flask application instance
    :param user_model: Model that contains the authentication information
    :type user_model: SQLAlchemy model
    :return: None
    """
    login_manager.login_message = 'Please login to access this page.'
    login_manager.login_view = 'auth.login'
    login_manager.session_protection = 'strong'
    login_manager.login_message_category = 'danger'

    @login_manager.user_loader
    def load_user(user_id):
        return user_model.query.get(int(user_id))


def blueprints(app):
    """
    Register 0 or more blueprints (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    for blueprint in FLASK_BLUEPRINTS:
        app.register_blueprint(blueprint)

    return None


def extensions(app):
    """
    Register 0 or more flask extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    bootstrap.init_app(app)
    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    return None
