'''
    SignOut.py Lib
    Written By Kyle Chen
    Version 20190418v1
'''

# import buildin pkgs
import os
from flask_restful import Resource
from flask_login import login_user, login_required, logout_user
from flask import redirect, request, \
                    render_template, Response, \
                    url_for, session

## import priviate pkgs
from app.models.User import User

## Sign Out Class
class SignOut(Resource):
    ## get method
    def get(self):
        return(Response('LogOut api'))
