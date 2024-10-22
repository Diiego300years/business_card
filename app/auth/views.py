from flask import render_template, request, url_for, flash, redirect, current_app
from . import auth
from flask_login import login_required, login_user, logout_user, current_user
from .forms import LoginForm, RegistrationForm
from app.models import User, Admin
from app import db
from app.main.utils.utils import send_email
from sqlalchemy.exc import IntegrityError

from .utils.utils import admin_required


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle user login for both Admin and regular users.

    Checks the submitted email and password against Admin and User records.
    If valid, logs the user in and redirects them to the next page (or home if none).
    If invalid, shows an error message and reloads the login page.

    Returns:
        - Redirect to 'next' or home on success.
        - Renders the login page with an error message on failure.
    """

    form = LoginForm()

    if form.validate_on_submit():
        my_user =  Admin.query.filter_by(email=form.email.data).first()
        # my_user = User.query.filter_by(email=form.email.data).first()
        if my_user is None:
            my_user = User.query.filter_by(email=form.email.data).first()


        if my_user is not None and my_user.check_password(password=form.password.data):
            login_user(my_user, form.remember_me.data)
            go_next = request.args.get('next')

            if go_next is None or not go_next.startswith('/'):
                go_next = url_for('main.index')
            return redirect(go_next)
        else:
            print("UWAGAAA  go_next is None or not go_next.startswith('/')")
        flash("email or password invalid")
    return render_template('auth/login.html', form=form)


# register for admin. For now need to stay
# @auth.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         admin = Admin(
#             name = form.username.data,
#             email = form.email.data,
#             # below used setter
#             password = form.password.data)
#         db.session.add(admin)
#         db.session.commit()
#         token = admin.generate_confirmation_token()
#         send_email(admin.email, 'confirm your account',
#                    'auth/email/confirm', admin=admin, token=token,)
#         flash('Check out your email address where you have to confirm your data.')
#         return redirect(url_for('main.index'))
#     return render_template('auth/register.html', form=form)

#register form for users
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
           # it's not necessary to check this email. Why? look at forms and validate_email method.
            my_user = User(
                name = form.username.data,
                email = form.email.data.lower(),
                commentator = True,
                # below used setter
                password = form.password.data,
            )
            db.session.add(my_user)
            db.session.commit()
            token = my_user.generate_confirmation_token()
            send_email(
                my_user.email,
                'confirm your account',
                'auth/email/confirm',
                my_user=my_user,
                token=token,
            )
            flash('Confirmation email has been sent to your email.')
            return redirect(url_for('main.index'))

        except IntegrityError as e:
            db.session.rollback()  # Session rollback if sth is wrong
            # Opcjonalnie, w trybie deweloperskim, wyświetl dodatkowy komunikat
            if current_app.config['FLASK_ENV'] == 'development':
                print(f"IntegrityError: {e}")
            return render_template('404.html')
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    try:
        if current_user.confirmed:
            return redirect(url_for('main.index'))
        try:

            if current_user.confirm_token(token):
                db.session.commit()
                flash('You confirmed your account! Thank you.')
            else:
                flash('Link address is not correct')
        except Exception as e:
            print("teraz coś tez bobki BOBKI z: ", e)
    except Exception as e:
        print("nie DZIAŁA confirm(token)", e)
    return redirect(url_for('main.index'))

@auth.route('/logout')
@login_required
def logout():
    user_name = current_user.name
    logout_user()
    flash(f'Bye {user_name}')
    return redirect(url_for('main.index'))


@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
        and not current_user.confirmed \
        and request.blueprint != 'auth' \
        and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')



@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'confirm your account',
               'auth/email/confirm', my_user=current_user, token=token, )
    flash('New email has been sent.')
    return redirect(url_for('main.index'))

# @auth.route('/secret')
# @login_required
# @admin_required
# def secret():
#     return 'Nice!'
