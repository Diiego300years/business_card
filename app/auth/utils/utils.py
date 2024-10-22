from functools import wraps
from flask import abort
from flask_login import current_user
from app.models.admin import Admin
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address


def admin_required(f):
    """
    A decorator to restrict access to routes to admin users only.

    Args:
      f (function): The original view function to be decorated.

    Returns:
        function: The wrapped function that checks if the user is an admin.
        If the user is not an admin, it aborts with a 403 error.

    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not isinstance(current_user, Admin):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


# Object with config
# limiter = Limiter(
#     app,
#     key_func=get_remote_address,  # user IP
#     default_limits=["200 per day", "50 per hour"]  # My global limits
# )


# my sample endpoint for this
# @app.route('/login', methods=['POST'])
# @limiter.limit("5 per minute")  # Ograniczenie: 5 prób logowania na minutę
# def login():
#     form = LoginForm()
#
#     if form.validate_on_submit():
#         my_user = Admin.query.filter_by(email=form.email.data).first()
#         if my_user is None:
#             my_user = User.query.filter_by(email=form.email.data).first()
#
#         if my_user is not None and my_user.check_password(password=form.password.data):
#             login_user(my_user, form.remember_me.data)
#             go_next = request.args.get('next')
#             if go_next is None or not go_next.startswith('/'):
#                 go_next = url_for('main.index')
#             return redirect(go_next)
#
#         flash("Invalid email or password")
#
#     return render_template('auth/login.html', form=form)