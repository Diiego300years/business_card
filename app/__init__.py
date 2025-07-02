from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_pagedown import PageDown
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from flask_mail import Mail
from flask_moment import Moment
from app.admin import AdminModelView, HomeEditorAdminView
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

# I decided to use several configuration sets
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bcrypt.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    pagedown.init_app(app)
    csrf.init_app(app)
    jwt.init_app(app)
    admin.init_app(app)

    from .auth.login_manager import login_manager
    login_manager.init_app(app)

    # add view to flask-admin
    from app.models.cms.home_editor import HomeEditor, ProjectsEditor
    # admin.add_view(AdminModelView(HomeEditor, db.session))
    admin.add_view(AdminModelView(ProjectsEditor, db.session, name="Projects Editor"))
    admin.add_view(HomeEditorAdminView(HomeEditor, db.session, name="Home Editor"))

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')


    return app


# application = create_app(config_name='default')
