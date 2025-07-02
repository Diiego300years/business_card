from flask import Flask
from app.admin import AdminModelView, HomeEditorAdminView
from config import config
import os
from app.admin import admin
from app.admin.views import MyAdminIndexView
from app.extensions import db, bcrypt, bootstrap, mail, moment, csrf, pagedown, migrate, jwt



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

    # global .env
    # app.jinja_env.globals['tinymce_api_key'] = os.getenv('TINYMCE_API_KEY')


    return app


# application = create_app(config_name='default')
