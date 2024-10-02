from flask import render_template, current_app, flash, redirect, url_for
from flask_mail import Message
from app import mail
from app.models.user import User
from app import db
from threading import Thread


# here can be also used @copy_current_app_context, then only one param=msg
# other option is celery for bigger applications @celery.task
def send_async_email(app,msg):
    """
    :param app: current_app
    :param msg: instance of Message
    :return: send message but None also for now
    """
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    """
    :param to: person which should get the message
    :param subject: subject of message
    :param template: path to txt and html
    :param kwargs: other params like variables for Jinja2
    :return: new thread which won't block main app's thread.
    """
    current_app.config["FLASKY_MAIL_SUBJECT_PREFIX"] = "BC"
    msg = Message(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    #mail.send(msg)

    # Below IDE issue
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app,msg])
    thr.start()
    return thr


# Fast function for delete
def delete_user(email):
    # Find user by email
    user = User.query.filter_by(email=email).first()

    if user:
        db.session.delete(user)
        db.session.commit()
        flash('User has been deleted')
    else:
        flash("I don't see user with this email.")

    return redirect(url_for('main.contact_handle'))
