from app import login_manager
from .admin import Admin

@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(str(admin_id))
