from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown
from flask_wtf import CSRFProtect

from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
pagedown = PageDown()
login_manager = LoginManager()
# login_manager.login_view = 'auth.login'


# I decided to use several configuration sets
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    pagedown.init_app(app)
    CSRFProtect(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
