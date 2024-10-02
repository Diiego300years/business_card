from flask import render_template, session, flash, redirect, url_for, current_app
from . import main
from .forms import ProspectDataForm, NameForm
from app.models.user import User
from app import db
from .utils.utils import send_email
from datetime import datetime


# home root for about me probably
@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('base.html')


# here I'll need to list github projects
@main.route('/projects', methods=['GET', 'POST'])
def handle_projects():
    """
    :return: view with my projects listed
    """
    user_name = session.get('name')
    return render_template('projects.html', name=user_name)


# simple endpoint for try flash()
@main.route("/try_flash", methods=['GET', 'POST'])
def check_name():
    form = NameForm()

    if form.validate_on_submit():
        old_name = session.get('name')

        if old_name is not None and old_name != form.name.data:
            flash("Well, that's new name")

        session['name'] = form.name.data
        return redirect(url_for('main.check_name'))

    return render_template('index_dwa.html', form=form, name=session.get('name'))


# endpoint for handling contact form. It should send email to Admin with information about new user.
# In the future I'll send client, my user's message.
@main.route("/contact", methods=['GET', 'POST'])
def contact_handle():
    """
    :return: Redirect after POST pattern
    """
    form = ProspectDataForm()
    if form.validate_on_submit():
        # for tests emails only
        #delete_prospect(form.e_mail.data)

        user = User.query.filter_by(name=form.e_mail.data).first()

        if user is None:
            # adding new user
            user = User(name=form.name.data,
                                email=form.e_mail.data,
                                message=form.message.data
                                )
            db.session.add(user)
            db.session.commit()
            session['known'] = False

            # Remember about using current_app !
            if current_app.config['FLASKY_ADMIN']:

                #email for prospect
                send_email(form.e_mail.data, '- z mojej apki Business card',
                           'mail/welcome_user',
                           user=user)

                #email for admin
                send_email(current_app.config['FLASKY_ADMIN'], '- z mojej apki Business card',
                           'mail/new_user',
                           user=user)
        else:
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.contact_handle'))

    # TODO: Think about what should I do with session['name']
    # print(session['name'])
    return render_template('index.html',
                           form=form,
                           name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())

