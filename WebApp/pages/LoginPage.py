'''
    LoginPage.py Lib
    Written By Kyle Chen
    Version 20190401v1
'''

# import buildin pkgs
import os
from flask import render_template
from flask_restful import Resource
from flask_login import login_required

## import priviate pkgs
from LoginForm import LoginForm

## Login Class
class LoginPage(Resource):
    ## get method
    def get(self):
        form = LoginForm()
        ## STOPPED HERE

        return(render_template('login.html'))

    ## post method
    def post(self):
        form = LoginForm()
        return(render_template('login.html'))
