'''
    AssetRelChart1.py Lib
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
class AssetRelChart1(Resource):
    ## get method
    @login_required
    def get(self):
        ## get OS info
        os_data = db.session.query(cmdb_OS).filter(cmdb_OS.hostname == 'srv1').first()
        hostname_val = os_data.hostname
        id_os_val = os_data.id
        os_id = re.sub('^OS-', '', id_os_val)
        os_dict_list = [ {'name': id_os_val} ]

        ## get DOCKER info
        docker_data = db.session.query(cmdb_DOCKER).filter(cmdb_DOCKER.id_os == str(id_os_val)).all()
        docker_dict_list = [ {'name': line.container_name} for line in docker_data ]

        ## get USER info
        user_data = db.session.query(cmdb_USER).filter(cmdb_USER.id_os == str(id_os_val)).all()
        user_dict_list = [ {'name': line.user_name} for line in user_data ]

        ## get GROUP info
        group_data = db.session.query(cmdb_GROUP).filter(cmdb_GROUP.id_os == str(id_os_val)).all()
        group_dict_list = [ {'name': line.group_name} for line in group_data ]

        ## get NETI info
        neti_data = db.session.query(cmdb_NETI).filter(cmdb_NETI.id_os == str(id_os_val)).all()
        neti_uniq_list = [ line.interface for line in neti_data ]
        neti_dict_list = [ {'name': interface} for interface in neti_uniq_list ]

        ## get PART info
        part_data = db.session.query(cmdb_PART).filter(cmdb_PART.id_os == str(id_os_val)).all()
        part_dict_list = [ {'name': line.mount_point} for line in part_data ]

        ## get DEV info
        dev_data = db.session.query(cmdb_DEV).filter(cmdb_DEV.id_os == str(id_os_val)).all()
        dev_dict_list = [ {'name': line.disk} for line in part_data ]

        ## get PORT info
        port_data = db.session.query(cmdb_PORT).filter(cmdb_PORT.id_os == str(id_os_val)).all()
        port_dict_list = [ {'name': re.sub('PORT-{}-'.format(os_id), '', re.sub('CLIENT-', '', line.id))} for line in port_data ]

        ## get PROC info
        proc_data = db.session.query(cmdb_PROC).filter(cmdb_PROC.id_os == str(id_os_val)).all()
        proc_dict_list = [ {'name': line.pid} for line in proc_data ]

        data = {
            'name': hostname_val,
            'children': [
                {
                    'name': 'OS',
                    'children': os_dict_list
                },{
                    'name': 'DOCKER',
                    'children': docker_dict_list
                },{
                    'name': 'USER',
                    'children': user_dict_list
               },{
                   'name': 'GROUP',
                   'children': group_dict_list
                },{
                    'name': 'NETI',
                    'children': neti_dict_list
                },{
                    'name': 'PART',
                    'children': part_dict_list
                },{
                    'name': 'DEV',
                    'children': dev_dict_list
                },{
                    'name': 'PORT',
                    'children': port_dict_list
                },{
                    'name': 'PROC',
                    'children': proc_dict_list
               },
            ]
        }
        return(Response(render_template('AssetRelChart1.html', data = data)))

    @login_manager.user_loader
    def load_user(user_id):
        return(User.getUser(user_id))
