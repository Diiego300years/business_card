from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from flask_mail import Mail
from flask_moment import Moment
from config import config

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
pagedown = PageDown()
login_manager = LoginManager()
# login_manager.login_view = 'auth.login'

# I decided to use several configuration sets
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    pagedown.init_app(app)
    CSRFProtect(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
