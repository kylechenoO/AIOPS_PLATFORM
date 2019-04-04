from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    user_name = StringField('User Name', validators = [DataRequired()], render_kw = {'placeholder': 'USERNAME',
        'onfocus': "this.placeholder = '';",
        'onblur': "if (this.placeholder == '') {this.placeholder = 'USERNAME';}"})
    email = EmailField('Email', validators = [DataRequired()], render_kw = {'placeholder': 'EMAIL',
        'onfocus': "this.placeholder = '';",
        'onblur': "if (this.placeholder == '') {this.placeholder = 'EMAIL';}"})
    password = PasswordField('Password', validators = [DataRequired()], render_kw = {'placeholder': 'PASSWORD',
        'onfocus': "this.placeholder = '';",
        'onblur': "if (this.placeholder == '') {this.placeholder = 'PASSWORD';}"})
    repassword = PasswordField('Please input Password twice', validators = [DataRequired()], render_kw = {'placeholder': 'REINPUT PASSWORD',
        'onfocus': "this.placeholder = '';",
        'onblur': "if (this.placeholder == '') {this.placeholder = 'REINPUT PASSWORD';}"})
