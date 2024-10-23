from flask_admin import Admin, expose
from flask import redirect, url_for, request
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from .views import MyAdminIndexView

admin = Admin(name='My CMS Admin', template_mode='bootstrap3', index_view=MyAdminIndexView(), base_template='admin/index.html')


class AdminModelView(ModelView):
    def is_accessible(self):
        from app.models.admin import Admin as MyAdmin
        return current_user.is_authenticated and isinstance(current_user, MyAdmin)

    def inaccessible_callback(self, name, **kwargs):
        # if he's not admin...
        return redirect(url_for('auth.login', next=request.url))

    @expose('/option1')
    def option1(self):
        return self.render('admin/homeeditor_option1.html')

    # Dodatkowa opcja 2
    @expose('/option2')
    def option2(self):
        return self.render('admin/homeeditor_option2.html')