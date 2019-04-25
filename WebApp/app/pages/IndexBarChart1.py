'''
    IndexBarChart1.py Lib
    Written By Kyle Chen
    Version 20190425v1
'''

# import buildin pkgs
import os
import json
from flask_restful import Resource
from flask_login import LoginManager
from flask_login import login_required
from flask import render_template, Response, url_for, jsonify

## import priviate pkgs
from app.models.User import User
from app.models.cmdb_OS import cmdb_OS
from app.models.cmdb_USER import cmdb_USER
from app.models.cmdb_NETI import cmdb_NETI
from app.models.cmdb_PART import cmdb_PART
from app.models.cmdb_PORT import cmdb_PORT
from app.models.cmdb_PROC import cmdb_PROC
from app.models.cmdb_GROUP import cmdb_GROUP
from app.models.cmdb_DOCKER import cmdb_DOCKER
from app import db, login_manager

## global values

## Index Class
class IndexBarChart1(Resource):
    ## get method
    @login_required
    def get(self):
        container_num = db.session.query(cmdb_DOCKER).count()
        vmware_num = db.session.query(cmdb_OS).filter_by(hardware_type = 'VMware Virtual Platform').count()
        hardware_num = db.session.query(cmdb_OS).filter(~cmdb_OS.hardware_type.in_(['VMware Virtual Platform', 'Container'])).count()
        os_num = db.session.query(cmdb_OS).count()
        user_num = db.session.query(cmdb_USER).count()
        group_num = db.session.query(cmdb_GROUP).count()
        neti_num = db.session.query(cmdb_NETI).count()
        part_num = db.session.query(cmdb_PART).count()
        port_num = db.session.query(cmdb_PORT).count()
        proc_num = db.session.query(cmdb_PROC).count()
        return Response(render_template('IndexBarChart1.html', container_num = container_num, vmware_num = vmware_num,
                                        hardware_num = hardware_num, os_num = os_num, user_num = user_num,
                                        group_num = group_num, neti_num = neti_num, part_num = part_num,
                                        port_num = port_num, proc_num = proc_num))

    @login_manager.user_loader
    def load_user(user_id):
        return(User.getUser(user_id))
