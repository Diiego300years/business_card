from dotenv import load_dotenv
from flask import Flask
from flask_smorest import Api
from .configuration.config import FlaskAppConfigurator

load_dotenv()

app = Flask(__name__)

# Configuration for app
configurator = FlaskAppConfigurator(app)
configurator.load_configuration()
configurator.configure_logging()

api = Api(app)

# Register blueprints
from .views.home import blp as HomeBluePrint
api.register_blueprint(HomeBluePrint)
# api.register_blueprint() if I need more
