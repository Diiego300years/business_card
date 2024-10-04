import os
from app import create_app, db
from app.models.user import User
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

#TODO: ADD OTHER models to Flask shell
@app.shell_context_processor
def make_shell_context():**********
 +-

@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)



