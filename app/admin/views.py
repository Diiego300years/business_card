from flask_admin import AdminIndexView
from flask_admin import expose
from flask_login import current_user
from flask import redirect, url_for, request



class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        from app.models.admin import Admin as MyAdmin
        return current_user.is_authenticated and isinstance(current_user, MyAdmin)

    def inaccessible_callback(self, name, **kwargs):
        # if he's not admin...
        return redirect(url_for('auth.login', next=request.url))

    @expose('/')
    def index(self):
        # cuz index is my base
        return self.render('admin/home.html')



