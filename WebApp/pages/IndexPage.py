'''
    IndexPage.py Lib
    Written By Kyle Chen
    Version 20190415v1
'''

# import buildin pkgs
import os
from flask_restful import Resource
from flask_login import LoginManager
from flask_login import login_required
from flask import render_template, Response, url_for

## import priviate pkgs
from models.User import User
from models.cmdb_OS import cmdb_OS
from models.cmdb_PORT import cmdb_PORT
from models.cmdb_PROC import cmdb_PROC
from models.cmdb_DOCKER import cmdb_DOCKER
from models.Global import db, login_manager

## global values

## Index Class
class IndexPage(Resource):
    ## get method
    @login_required
    def get(self):
        number_os = db.session.query(cmdb_OS).count()
        number_container = db.session.query(cmdb_DOCKER).count()
        number_port = db.session.query(cmdb_PORT).count()
        number_proc = db.session.query(cmdb_PROC).count()
        return(Response(render_template('Index.html', signout_url = url_for('signoutpage'),
            number_os = number_os, number_container = number_container,
            number_port = number_port, number_proc = number_proc)))

    @login_manager.user_loader
    def load_user(user_id):
        return(User.getUser(user_id))
