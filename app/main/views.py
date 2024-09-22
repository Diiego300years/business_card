from flask import render_template, session, flash, redirect, url_for
from . import main
from .forms import NameForm

# home root for about me probably
@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('base.html')


# here I'll need to list github projects
@main.route('/projects', methods=['GET', 'POST'])
def handle_projects():
    user_name = session.get('name')
    return render_template('projects.html', name=user_name)


# simple endpoint for concat form
@main.route("/wtf", methods=['GET', 'POST'])
def check_name():
    form = NameForm()

    if form.validate_on_submit():
        old_name = session.get('name')

        if old_name is not None and old_name != form.name.data:
            flash("Well, that's new name")

        session['name'] = form.name.data
        return redirect(url_for('main.check_name'))

    return render_template('index.html', form=form, name=session.get('name'))
