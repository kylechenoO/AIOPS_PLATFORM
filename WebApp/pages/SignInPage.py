'''
    SignInPage.py Lib
    Written By Kyle Chen
    Version 20190401v2
'''

# import buildin pkgs
import os
from flask_restful import Resource
from flask_login import login_user, login_required
from flask import redirect, request, \
                    render_template, Response, \
                    url_for

## import priviate pkgs
from SignInForm import SignInForm
from UserMod import UserMod

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

            userObj = UserMod(user_name)
            result = userObj.getPassword()
            if result == password:
                return(Response('Login Successful'))

        return(Response(render_template('SignIn.html', title="Sign In", form = form)))
