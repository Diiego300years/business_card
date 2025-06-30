from flask_login import LoginManager
from app.models.admin import Admin
from app.models.user import User

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Wpierw się zaloguj!'
login_manager.login_message_category = "warning"

@login_manager.user_loader
def load_user(user_id):
    my_user = User.query.get(str(user_id))

    if my_user is None:
        return Admin.query.get(str(user_id))
    return my_user