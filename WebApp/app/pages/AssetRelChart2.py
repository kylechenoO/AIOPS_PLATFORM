'''
    AssetRelChart2.py Lib
    Written By Kyle Chen
    Version 20190426v1
'''

# import buildin pkgs
import re
from flask_restful import Resource
from flask_login import login_required
from flask import render_template, Response

## import priviate pkgs
from app.models.User import User
from app.models.cmdb_OS import cmdb_OS
from app.models.cmdb_USER import cmdb_USER
from app.models.cmdb_GROUP import cmdb_GROUP
from app.models.cmdb_NETI import cmdb_NETI
from app.models.cmdb_PART import cmdb_PART
from app.models.cmdb_DEV import cmdb_DEV
from app.models.cmdb_PORT import cmdb_PORT
from app.models.cmdb_PROC import cmdb_PROC
from app.models.cmdb_DOCKER import cmdb_DOCKER
from app import db, login_manager

## Index Class
class AssetRelChart2(Resource):
    ## get method
    @login_required
    def get(self):
        ## get OS info
        os_data = db.session.query(cmdb_OS).filter(cmdb_OS.hostname == 'srv1').first()
        hostname_val = os_data.hostname
        id_os_val = os_data.id
        os_id = re.sub('^OS-', '', id_os_val)
        os_dict_list = [ {'name': id_os_val} ]

        ## get PORT info
        port_data = db.session.query(cmdb_PORT).filter(cmdb_PORT.id_os == str(id_os_val)).all()
        port_dict_list = [ {'name': re.sub('PORT-{}-'.format(os_id), '', re.sub('CLIENT-', '', line.id))} for line in port_data ]

        data = {
            "nodes": [{
                "id": "0",
                "name": "srv1",
                "symbolSize": 10,
                "value": 1,
                "category": 0
            }, {
                "id": "1",
                "name": "srv2",
                "symbolSize": 10,
                "value": 4,
                "category": 1
            }],
            "links": [{
                "id": "0",
                "name": 'rel1',
                "source": "0",
                "target": "1",
            }]
        }
        return(Response(render_template('AssetRelChart2.html', data = data)))

    @login_manager.user_loader
    def load_user(user_id):
        return(User.getUser(user_id))
