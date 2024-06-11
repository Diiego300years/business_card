from flask_wtf import FlaskForm
from wtforms import StringField, \
    SubmitField
from wtforms.validators import DataRequired, Email
from flask_pagedown.fields import PageDownField

class NameForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    surname = StringField('surname')
    e_mail = StringField("e-mail", validators=[Email()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    body = PageDownField("What's on your mind?", validators=[DataRequired()])
    submit = SubmitField('Submit')
