from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_pagedown import PageDown
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from flask_mail import Mail
from flask_moment import Moment
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt


jwt = JWTManager()
bcrypt = Bcrypt()
bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
csrf = CSRFProtect()
pagedown = PageDown()
