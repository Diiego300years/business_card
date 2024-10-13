from . import login_manager
from models.admin import Admin

@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(int(admin_id))
