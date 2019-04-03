'''
    IndexPage.py Lib
    Written By Kyle Chen
    Version 20190403v1
'''

# import buildin pkgs
import os
from flask_restful import Resource
from flask_login import LoginManager
from flask_login import login_required
from flask import render_template, Response, session

## import priviate pkgs
from models.Global import login_manager
from models.User import User

## global values

## Index Class
class IndexPage(Resource):
    ## get method
    @login_required
    def get(self):
        if not session['login_flag']:
            session['login_flag'] = False

        if not session['user_name']:
            session['user_name'] = False

        return(Response(render_template('Index.html')))

    @login_manager.user_loader
    def load_user(user_id):
        return(User.getUser(user_id))
