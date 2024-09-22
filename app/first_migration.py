from flask_migrate import Migrate
from app import create_app, db
app = create_app('development' or 'default')
migrate = Migrate(app, db)
