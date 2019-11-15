import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))


class Config(object):
    """
    Common configurations
    """
    SECRET_KEY = os.getenv('SECRET_KEY') or 'dev'

    # Track modifications of objects and emit signals
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(BASE_DIR, 'dreamteam.db')


class ProdConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class TestConfig(Config):
    """
    Testing configurations
    """

    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(BASE_DIR, 'dreamteam.db_test')
    WTF_CSRF_ENABLED = False


app_config = {
    'development': DevConfig,
    'production': ProdConfig,
    'testing': TestConfig
}
