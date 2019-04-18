'''
    cmdb_DOCKER.py Lib
    Written By Kyle Chen
    Version 20190418v1
'''

# import buildin pkgs

## import priviate pkgs
from app import db

## cmdb_DOCKER Class
class cmdb_DOCKER(db.Model):
    __tablename__ = 'cmdb_DOCKER'
    id = db.Column('id', db.String(128), primary_key = True, nullable = False, unique = True)
    id_os = db.Column(db.String(128))
    run_time = db.Column(db.Date)
    container_id = db.Column(db.String(128))
    container_name = db.Column(db.String(128))
    image_name = db.Column(db.String(128))
    stats = db.Column(db.String(16))
    status = db.Column(db.String(64))
    port_dict = db.Column(db.Text)
    network_setting_dict = db.Column(db.Text)
    disk_dict = db.Column(db.Text)
    insert_time = db.Column(db.Date)
    update_time = db.Column(db.Date)
