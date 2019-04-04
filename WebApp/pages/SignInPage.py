'''
    SignInPage.py Lib
    Written By Kyle Chen
    Version 20190403v1
'''

# import buildin pkgs
import os
from flask_restful import Resource
from flask_login import login_user, login_required
from flask import redirect, request, \
                    render_template, Response, \
                    url_for, session

## import priviate pkgs
from views.SignInForm import SignInForm
from models.User import User

## Sign In Class
class SignInPage(Resource):
    ## get method
    def get(self):
        form = SignInForm()
        return(Response(render_template('SignIn.html', title="Sign In", form = form)))

    ## post method
    def post(self):
        form = SignInForm()
        if form.validate_on_submit():
            user_name = request.form.get('user_name', None)
            password = request.form.get('password', None)
            remember_me = request.form.get('remember_me', False)
            userObj = User(user_name)
            if userObj.verifyPassword(password):
                login_user(userObj, remember = remember_me)
                userObj.is_authenticated = True
                session['user_name'] = user_name
                return(redirect(url_for('indexpage')))

        return(Response(render_template('SignIn.html', title="Sign In", form = form, message = 'Password Error')))
