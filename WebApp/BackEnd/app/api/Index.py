'''
    Index.py Lib
    Written By Kyle Chen
    Version 20190418v1
'''

# import buildin pkgs
import os
from flask_restful import Resource
from flask_login import LoginManager
from flask_login import login_required
from flask import render_template, Response, url_for

## import priviate pkgs
from app.models.User import User
from app.models.cmdb_OS import cmdb_OS
from app.models.cmdb_PORT import cmdb_PORT
from app.models.cmdb_PROC import cmdb_PROC
from app.models.cmdb_DOCKER import cmdb_DOCKER
from app import db, login_manager

## Index Class
class Index(Resource):
    ## get method
    def get(self):
        return(Response('Index api'))
