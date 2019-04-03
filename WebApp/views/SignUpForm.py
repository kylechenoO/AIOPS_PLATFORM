from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    user_name = StringField('User Name', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    repassword = PasswordField('Please input Password twice', validators = [DataRequired()])
