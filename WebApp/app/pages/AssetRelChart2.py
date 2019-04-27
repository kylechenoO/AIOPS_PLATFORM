'''
    AssetRelChart2.py Lib
    Written By Kyle Chen
    Version 20190427v1
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
        os_data = db.session.query(cmdb_OS.id, cmdb_OS.hostname).filter(cmdb_OS.hostname == 'srv1').first()
        hostname_val = os_data.hostname
        id_os_val = os_data.id
        os_id = re.sub('^OS-', '', id_os_val)
        os_dict_list = [{'name': id_os_val}]

        ## get all ips
        ip_data = db.session.query(cmdb_OS.id, cmdb_OS.hostname, cmdb_OS.ip_list).all()
        ip_dict = { ip:line.hostname for line in ip_data for ip in re.split(',', line.ip_list) if ip not in ['127.0.0.1', '::1'] }
        ip_dict['127.0.0.1'] = hostname_val
        ip_dict['::1'] = hostname_val

        ## get PORT info
        port_data = db.session.query(cmdb_PORT.id, cmdb_PORT.status, cmdb_PORT.dst_ip,
                                     cmdb_PORT.dst_port).filter(cmdb_PORT.id_os == str(id_os_val)).all()
        port_established = [ (re.sub('PORT-CLIENT-{}-'.format(os_id), '', line.id),
                              ip_dict[line.dst_ip] if line.dst_ip in ip_dict.keys() else line.dst_ip,
                              line.dst_port) for line in port_data if line.status == 'ESTABLISHED' ]
        print('port_est [{}]'.format(port_established))
        port_dict_list = [ {'name': line[0], 'children': [{'name': '{}-{}'.format(line[1], line[2])}]} for line in port_established ]

        data = {
            'name': hostname_val,
            'children': port_dict_list
        }
        return(Response(render_template('AssetRelChart2.html', data = data)))

    @login_manager.user_loader
    def load_user(user_id):
        return(User.getUser(user_id))
