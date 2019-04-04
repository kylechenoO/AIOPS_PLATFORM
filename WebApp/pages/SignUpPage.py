'''
    SignUpPage.py Lib
    Written By Kyle Chen
    Version 20190401v1
'''

# import buildin pkgs
from flask_restful import Resource
from flask_login import login_user
from flask import redirect, request, \
                    render_template, Response, \
                    url_for

## import priviate pkgs
from views.SignUpForm import SignUpForm
from models.User import User

## Sign Up Class
class SignUpPage(Resource):
    ## get method
    def get(self):
        form = SignUpForm()
        return(Response(render_template('SignUp.html', title="Sign Up", form = form)))

    ## post method
    def post(self):
        form = SignUpForm()
        if form.validate_on_submit():
            user_name = request.form.get('user_name', None)
            email = request.form.get('email', None)
            password = request.form.get('password', None)
            repassword = request.form.get('repassword', None)

            if user_name is None:
                return(Response(render_template('SignUp.html', title="Sign Up", form = form, message = 'Please fill in the User Name')))

            if email is None:
                return(Response(render_template('SignUp.html', title="Sign Up", form = form, message = 'Please fill in the Email')))

            if password is None or repassword is None:
                return(Response(render_template('SignUp.html', title="Sign Up", form = form, message = 'Please fill in the Password')))

            if password == repassword:
                userObj = User(user_name = user_name, password = password, email = email)
                if userObj.createUser():
                    return(Response(render_template('SignIn.html', title="Sign In", form = form, message = 'Please Login')))

                else:
                    return(Response(render_template('SignUp.html', title="Sign Up", form = form, message = 'Sign Up Error')))

            else:
                return(Response(render_template('SignUp.html', title="Sign Up", form = form, message = "Password didn't match")))
