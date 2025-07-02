from flask_admin import AdminIndexView
from flask_admin import expose
from flask_login import current_user
from flask import redirect, url_for, request
from dotenv import load_dotenv
from app.models.user import User
import os

load_dotenv()


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        from app.models.admin import Admin as MyAdmin
        return current_user.is_authenticated and isinstance(current_user, MyAdmin)

    def inaccessible_callback(self, name, **kwargs):
        # if he's not admin...
        return redirect(url_for('auth.login', next=request.url))

    @expose('/')
    def index(self):
        TINYMCE_API_KEY = os.getenv('TINYMCE_API_KEY')
        stats = {
            'users': User.query.count(),
        }
        return self.render('admin/home.html', tinymce_api_key=TINYMCE_API_KEY)
