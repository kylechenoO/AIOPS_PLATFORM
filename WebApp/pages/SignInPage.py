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
            user_name = request.form.get('username', None)
            password = request.form.get('password', None)
            remember_me = request.form.get('remember_me', False)
            ## user1 for test user
            ## STOPPED HERE NEED TO CONNECT TO DB AND CHECK USER INFO
            if user_name == 'user1' and password == 'user1':
                login_user('user1')
                redirect(request.args.get('next') or url_for('indexpage'))

            return(Response(render_template('SignIn.html', title="Sign In", form = form)))
