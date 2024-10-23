from flask import Flask, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_pagedown import PageDown
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from flask_mail import Mail
from flask_moment import Moment
from app.admin import AdminModelView
from config import config
from flask_bcrypt import Bcrypt
import os
from flask_jwt_extended import JWTManager
from app.admin import admin
from app.admin.views import MyAdminIndexView


jwt = JWTManager()
bcrypt = Bcrypt()
bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
csrf = CSRFProtect()
pagedown = PageDown()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

# I decided to use several configuration sets
def create_app(config_name):
    config_name = os.getenv('FLASK_CONFIG', 'default')
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bcrypt.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    pagedown.init_app(app)
    csrf.init_app(app)
    jwt.init_app(app)
    admin.init_app(app)

    # add view to flask-admin
    from app.models.cms.home_editor import HomeEditor
    admin.add_view(AdminModelView(HomeEditor, db.session))

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .cms import cms as cms_blueprint
    app.register_blueprint(cms_blueprint, url_prefix='/cms')


    return app


# application = create_app(config_name='default')
