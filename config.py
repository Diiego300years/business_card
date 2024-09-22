import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.getcwd(), '.env'))

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'qwer'

    @staticmethod
    def init_app(app):
        pass


# TODO: Add real database paths to .env
class DevelopmentConfig(Config):
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    FLASK_APP=os.environ.get('FLASK_APP')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30
    FLASKY_SLOW_DB_QUERY_TIME = 0.5



class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')
    WTF_CSRF_ENABLED = False


# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    # 'production': ProductionConfig,
    'default': DevelopmentConfig
}
