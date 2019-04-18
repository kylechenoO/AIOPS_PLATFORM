'''
    SignIn.py Lib
    Written By Kyle Chen
    Version 20190418v1
'''

# import buildin pkgs
import os
from flask_restful import Resource
from flask_login import login_user, login_required
from flask import redirect, request, \
                    render_template, Response, \
                    url_for, session

## import priviate pkgs
from app.models.User import User

## Sign In Class
class SignIn(Resource):
    ## get method
    def get(self):
        return(Response('SignIn api'))

    ## post method
    def post(self):
        return(Response('SignIn api'))
