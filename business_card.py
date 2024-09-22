# import os
# from app import create_app, db
# from flask_migrate import Migrate
# from app.models.admin import Admin
# from app.models.prospect import Prospect
#
# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# # migrate = Migrate(app, db)
#
# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db, Admin=Admin, Prospect=Prospect)


import os

from dotenv import load_dotenv
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from config import config

load_dotenv()

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
pagedown = PageDown()
login_manager = LoginManager()
# login_manager.login_view = 'auth.login'


# I decided to use several configuration sets
def create_app(config_name):
    app = Flask(os.getenv('FLASK_APP_NAME'))
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    pagedown.init_app(app)
    CSRFProtect(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
