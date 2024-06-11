from flask import render_template
from . import main
from .forms import NameForm

# home root for about me probably
@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('base.html')


# here I'll need to list github projects
@main.route('/projects', methods=['GET', 'POST'])
def handle_projects():
    return render_template('projects.html')


# simple endpoint for concat
@main.route("/wtf", methods=['GET', 'POST'])
def check_name():
    name = None
    form = NameForm()

    if form.validate_on_submit():
        form.e_mail.data = ''
        name = form.name.data
        form.name.data = ''
        form.surname.data = ''

    return render_template('index.html', form=form, name=name)
