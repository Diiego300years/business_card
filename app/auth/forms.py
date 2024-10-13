from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('e-mail', validators=[DataRequired(),
                        Length(1,64),
                        Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(8,64)])
    remember_me = BooleanField('Remember me')
    submite = SubmitField('Submite')