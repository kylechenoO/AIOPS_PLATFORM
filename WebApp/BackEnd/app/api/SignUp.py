'''
    SignUp.py Lib
    Written By Kyle Chen
    Version 20190418v1
'''

# import buildin pkgs
from flask_restful import Resource
from flask_login import login_user
from flask import redirect, request, \
                    render_template, Response, \
                    url_for

## import priviate pkgs
from app.models.User import User

## Sign Up Class
class SignUp(Resource):
    ## get method
    def get(self):
        return(Response('SignUp api'))

    ## post method
    def post(self):
        return(Response('SignUp api'))
