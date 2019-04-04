'''
    SignOutPage.py Lib
    Written By Kyle Chen
    Version 20190404v1
'''

# import buildin pkgs
import os
from flask_restful import Resource
from flask_login import login_user, login_required, logout_user
from flask import redirect, request, \
                    render_template, Response, \
                    url_for, session

## import priviate pkgs
from views.SignInForm import SignInForm
from models.User import User

## Sign Out Class
class SignOutPage(Resource):
    ## get method
    @login_required
    def get(self):
        session['user_name'] = None
        logout_user()
        return(redirect(url_for('indexpage')))
