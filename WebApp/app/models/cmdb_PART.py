'''
    cmdb_PART.py Lib
    Written By Kyle Chen
    Version 20190420v1
'''

# import buildin pkgs

## import priviate pkgs
from app import db

## cmdb_PART Class
class cmdb_PART(db.Model):
    __tablename__ = 'cmdb_PART'
    id = db.Column('id', db.String(128), primary_key = True, nullable = False, unique = True)
    id_os = db.Column(db.String(128))
    id_dev = db.Column(db.String(128))
    run_time = db.Column(db.Date)
    disk = db.Column(db.String(128))
    part = db.Column(db.String(128))
    type = db.Column(db.String(16))
    mounted = db.Column(db.String(8))
    mount_point = db.Column(db.String(512))
    size = db.Column(db.Integer)
    disk_usage = db.Column(db.String(16))
    insert_time = db.Column(db.Date)
    update_time = db.Column(db.Date)
