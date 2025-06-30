from flask import render_template, session, redirect, url_for, current_app
from . import main
from .forms import ProspectDataForm
from ..models.cms.home_editor import HomeEditor
from ..models.user import User
from app import db
from .utils.utils import send_email
from datetime import datetime
from flask_login import current_user
from ..models.admin import Admin


# home root for about me probably
@main.route('/', methods=['GET', 'POST'])
def index():
    """
    Renders the home page (index.html).

    :return: Rendered template for the home page.
    """
    empty_base = False
    try:
        home_data = HomeEditor.query.first()

        if home_data:
            empty_base = True
            data = {
                'title': home_data.title,
                'description': home_data.description,
                'added_at': home_data.added_at,
                'empty_base': empty_base
            }
            return render_template('index.html', **data)
        else:
            return render_template('index.html', empty_base=empty_base)
    except:
        return render_template('index.html', empty_base=empty_base)


# here I'll need to list gitHub projects
@main.route('/projects', methods=['GET', 'POST'])
def handle_projects():
    """
    Renders the projects page, listing the user's projects.
    The user's name is retrieved from the session.

    :return: Rendered template for the projects page with the user's name.
    """
    if session.get('name'):
        user_name = session.get('name')
        return render_template('projects.html', name=user_name)
    else:
        return render_template('projects.html')


# simple endpoint for try flash()
# @main.route("/try_flash", methods=['GET', 'POST'])
# def check_name():
#     """
#     Handles form submission to update the user's name in the session.
#     Flashes a message if the name is changed.
#
#     :return: If form is submitted and valid, redirects to the same page. Otherwise, renders the form.
#
#     """
#     form = NameForm()
#
#     if form.validate_on_submit():
#         old_name = session.get('name')
#
#         if old_name is not None and old_name != form.name.data:
#             flash("Well, that's new name")
#
#         session['name'] = form.name.data
#         return redirect(url_for('main.check_name'))
#
#     return render_template('index_dwa.html', form=form, name=session.get('name'))


# endpoint for handling contact form. It should send email to Admin with information about new user.
# In the future I'll send client, my user's message.
@main.route("/contact", methods=['GET', 'POST'])
def contact_handle():
    """
    Handles the contact form submission, stores a new user in the database if they don't exist,
    and sends an email to the user and admin. Updates session with the user's name and status.

    :return: If form is submitted and valid, redirects to the same page.
    Otherwise, renders the contact form with current data.
    """
    form = ProspectDataForm()
    if form.validate_on_submit():
        # for tests emails only
        #delete_prospect(form.e_mail.data)

        user = User.query.filter_by(name=form.e_mail.data).first()

        if user is None:
            # adding new user
            user = User(name=form.name.data,
                        email=form.e_mail.data.lower(),
                        message=form.message.data,
                        password = "YourPassword#1234"
                                )
            db.session.add(user)
            db.session.commit()
            session['known'] = False

            token = user.generate_confirmation_token()
            send_email(
                user.email,
                'Utwórz konto jeśli chcesz!',
                'mail/invitation',
                user=user,
                token=token,
            )

        else:
            #TODO: It's useless for now. I must change it
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.contact_handle'))

    # TODO: Think about what should I do with session['name']
    # print(session['name'])
    user_name = session.get('name')
    return render_template('contact.html',
                           form=form,
                           name=user_name,
                           current_time=datetime.utcnow())

@main.context_processor
def inject_user_role():
    is_admin = isinstance(current_user, Admin) if current_user.is_authenticated else False
    return {'is_admin': is_admin}
