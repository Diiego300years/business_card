from app import login_manager
from .admin import Admin
from .user import User

@login_manager.user_loader
def load_user(user_id):
    my_user = User.query.get(str(user_id))

    if my_user is None:
        return Admin.query.get(str(user_id))
    return my_user
