'''
    cmdb_PORT.py Lib
    Written By Kyle Chen
    Version 20190418v1
'''

# import buildin pkgs

## import priviate pkgs
from app import db

## cmdb_PORT Class
class cmdb_PORT(db.Model):
    __tablename__ = 'cmdb_PORT'
    id = db.Column('id', db.String(128), primary_key = True, nullable = False, unique = True)
    id_os = db.Column(db.String(128))
    id_user = db.Column(db.String(128))
    id_proc = db.Column(db.String(128))
    id_neti_list = db.Column(db.String(10240))
    rel_port_list = db.Column(db.String(10240))
    run_time = db.Column(db.Date)
    type = db.Column(db.String(16))
    listening_ip_list = db.Column(db.String(10240))
    port = db.Column(db.String(16))
    status = db.Column(db.String(16))
    pid = db.Column(db.String(16))
    neti_list = db.Column(db.String(256))
    user = db.Column(db.String(16))
    uid = db.Column(db.String(8))
    dst_ip = db.Column(db.String(16))
    dst_port = db.Column(db.String(16))
    insert_time = db.Column(db.Date)
    update_time = db.Column(db.Date)
