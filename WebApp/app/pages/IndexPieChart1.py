'''
    IndexPieChart1.py Lib
    Written By Kyle Chen
    Version 20190424v1
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

## global values

## Index Class
class IndexPieChart1(Resource):
    ## get method
    @login_required
    def get(self):
        container_num = db.session.query(cmdb_DOCKER).count()
        vmware_num = 1
        return Response(render_template('IndexPieChart1.html', container_num = container_num, vmware_num = vmware_num))

    @login_manager.user_loader
    def load_user(user_id):
        return(User.getUser(user_id))
