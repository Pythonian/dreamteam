from flask import Flask

from app.models import Department, Employee, Role
from app.register import (authentication, blueprints, extensions)
from config import app_config


def create_app(config_name):
    """
    Create a Flask application using the app factory pattern.

    http://flask.pocoo.org/docs/dev/patterns/appfactories

    :param config_name: The settings configuration to use
    :return: Flask app
    """
    app = Flask(__name__)

    app.config.from_object(app_config[config_name])
    app_config[config_name].init_app(app)

    # Register
    authentication(app, Employee)
    blueprints(app)
    extensions(app)

    # Shell context
    @app.shell_context_processor
    def make_shell_context():
        from .extensions import db
        """Create a shell context for all models."""
        return dict(db=db, Employee=Employee,
                    Department=Department, Role=Role)

    return app
