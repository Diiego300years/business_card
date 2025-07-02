from flask_admin import Admin, expose
from flask import redirect, url_for, request
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from wtforms import TextAreaField
from .views import MyAdminIndexView
import os
from dotenv import load_dotenv

load_dotenv()

admin = Admin(name='My CMS Admin', template_mode='bootstrap3', index_view=MyAdminIndexView(), base_template='admin/index.html')


class AdminModelView(ModelView):
    def is_accessible(self):
        from app.models.admin import Admin as MyAdmin
        return current_user.is_authenticated and isinstance(current_user, MyAdmin)

    def inaccessible_callback(self, name, **kwargs):
        # if he's not admin...
        return redirect(url_for('auth.login', next=request.url))


class HomeEditorAdminView(AdminModelView):
    column_searchable_list = ['title']

    form_overrides = {
        'content': TextAreaField
    }
    form_widget_args = {
        'description': {
            'class': 'tinymce'
        }
    }
    create_template = 'admin/edit_with_tinymce.html'
    edit_template = 'admin/edit_with_tinymce.html'

    # nadpisanie metod create oraz edit
    def render(self, template, **kwargs):
        # Dodajemy klucz tylko do wywołania renderowania tego widoku
        kwargs['tinymce_api_key'] = os.getenv('TINYMCE_API_KEY')
        return super().render(template, **kwargs)


# class ProjectsEditorAdminView(AdminModelView):
#     column_searchable_list = ['title']
#
#     form_overrides = {
#         'content': TextAreaField
#     }
#
#     # orm_widget_args = {
#     #     'description': {
#     #         'class': 'tinymce'
#     #     }
#     # }
#     create_template = 'admin/edit_projects.html'
#     edit_template = 'admin/edit_projects.html'
#
#     def render(self, template, **kwargs):
#         # Dodajemy klucz tylko do wywołania renderowania tego widoku
#         return super().render(template, **kwargs)
