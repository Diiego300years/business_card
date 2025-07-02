from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.admin import Admin
from app.models.cms.home_editor import HomeEditor, ProjectsEditor
from flask_migrate import Migrate
from dotenv import load_dotenv
import sys, os

sys.path.append(os.getcwd())

load_dotenv()

application = create_app(config_name='default')
migrate = Migrate(application, db)

@application.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Admin=Admin, ProjectsEditor=ProjectsEditor, HomeEditor=HomeEditor)

@application.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
