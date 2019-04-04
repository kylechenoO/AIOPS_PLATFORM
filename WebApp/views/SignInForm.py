from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class SignInForm(FlaskForm):
    user_name = StringField('User Name', validators = [DataRequired()], render_kw = {'placeholder': 'USERNAME',
        'onfocus': "this.placeholder = '';",
        'onblur': "if (this.placeholder == '') {this.placeholder = 'USERNAME';}"})
    password = PasswordField('Password', validators = [DataRequired()], render_kw = {'placeholder': 'PASSWORD',
        'onfocus': "this.placeholder = '';",
        'onblur': "if (this.placeholder == '') {this.placeholder = 'PASSWORD';}"})
    remember_me = BooleanField('remember me', default = False)
