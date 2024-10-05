import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.getcwd(), '.env'))

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    FLASKY_MAIL_SENDER = os.getenv("FLASKY_MAIL_SENDER")
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

    FLASKY_ADMIN = os.getenv("FLASKY_ADMIN")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    FLASK_APP=os.environ.get('FLASK_APP')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30
    FLASKY_SLOW_DB_QUERY_TIME = 0.5



class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    MAIL_SERVER = os.getenv('PROD_MAIL_SERVER')
    MAIL_PORT = os.getenv('PROD_MAIL_PORT')
    FLASKY_MAIL_SENDER = os.getenv("PROD_FLASKY_MAIL_SENDER")
    MAIL_USERNAME = os.getenv('PROD_MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('PROD_MAIL_PASSWORD')

    FLASKY_ADMIN = os.getenv("PROD_FLASKY_ADMIN")

    # @classmethod
    # def init_app(cls, app):
    #     Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
