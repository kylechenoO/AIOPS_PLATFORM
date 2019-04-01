from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    username = StringField('User Name', validators = [DataRequired()])
    password1 = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('Please input Password twice', validators = [DataRequired()])
