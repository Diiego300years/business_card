from flask_wtf import FlaskForm
from wtforms import StringField, \
    SubmitField
from wtforms.validators import DataRequired, Email
from flask_pagedown.fields import PageDownField

class NameForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    e_mail = StringField("e-mail", validators=[Email(), DataRequired()])
    submit = SubmitField('Submit')


class ProspectDataForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    e_mail = StringField("e-mail", validators=[Email(), DataRequired()])
    message = StringField("message", validators=[DataRequired()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    body = PageDownField("What's on your mind?", validators=[DataRequired()])
    submit = SubmitField('Submit')
