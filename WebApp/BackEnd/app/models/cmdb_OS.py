'''
    cmdb_OS.py Lib
    Written By Kyle Chen
    Version 20190418v1
'''

# import buildin pkgs

## import priviate pkgs
from app import db

## cmdb_OS Class
class cmdb_OS(db.Model):
    __tablename__ = 'cmdb_OS'
    id = db.Column('id', db.String(128), primary_key = True, nullable = False, unique = True)
    id_net_list = db.Column(db.String(10240))
    run_time = db.Column(db.Date)
    hardware_id = db.Column(db.String(128))
    hardware_type = db.Column(db.String(128))
    os_type = db.Column(db.String(16))
    os_version = db.Column(db.String(32))
    arch = db.Column(db.String(16))
    kernel = db.Column(db.String(32))
    hostname = db.Column(db.String(32))
    python_version = db.Column(db.String(16))
    installed_pkgs = db.Column(db.Text)
    ip_list = db.Column(db.String(1024))
    interface_list = db.Column(db.String(128))
    insert_time = db.Column(db.Date)
    update_time = db.Column(db.Date)
