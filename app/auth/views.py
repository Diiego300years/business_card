from flask import render_template, request, url_for, flash, redirect
from . import auth
from flask_login import login_required, login_user, logout_user, current_user
from .forms import LoginForm, RegistrationForm
from app.models.admin import Admin
from app import db
from app.main.utils.utils import send_email

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()
        if admin is not None and admin.check_password(form.password.data):
            login_user(admin, form.remember_me.data)
            go_next = request.args.get('next')
            if go_next is None or not go_next.startswith('/'):
                go_next = url_for('main.index')
            return redirect(go_next)
        flash("username or password invalid")
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        admin = Admin(
            name = form.username.data,
            email = form.email.data,
            # below used setter
            password = form.password.data)
        db.session.add(admin)
        db.session.commit()
        token = admin.generate_confirmation_token()
        send_email(admin.email, 'confirm your account',
                   'auth/email/confirm', admin=admin, token=token,)
        flash('Check out your email address where you have to confirm your data.')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm_token(token):
        db.session.commit()
        flash('You confirmed your account! Thank you.')
    else:
        flash('Link address is not correct')
    return redirect(url_for('main.index'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Bye')
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
               'auth/email/confirm', admin=current_user, token=token, )
    flash('New email has been sent.')
    return redirect(url_for('main.index'))

@auth.route('/secret')
@login_required
def secret():
    return 'Nice!'