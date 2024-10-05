import os
from app import create_app, db
from app.models.user import User
from app.models.admin import Admin
from app.models.user_base import UserBase
from app.models.projects import MyProjects
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Admin=Admin, MyProjects=MyProjects)

@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)



