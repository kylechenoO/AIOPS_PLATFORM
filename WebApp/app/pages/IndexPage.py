'''
    IndexPage.py Lib
    Written By Kyle Chen
    Version 20190420v1
'''

# import buildin pkgs
import os
from flask_restful import Resource
from flask_login import login_required
from flask import render_template, Response

## import priviate pkgs
from app.models.User import User
from app import login_manager

## global values

## Index Class
class IndexPage(Resource):
    ## get method
    @login_required
    def get(self):
        return(Response(render_template('Index.html')))

    @login_manager.user_loader
    def load_user(user_id):
        return(User.getUser(user_id))
