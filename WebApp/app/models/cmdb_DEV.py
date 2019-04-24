'''
    cmdb_DEV.py Lib
    Written By Kyle Chen
    Version 20190420v1
'''

# import buildin pkgs

## import priviate pkgs
from app import db

## cmdb_DEV Class
class cmdb_DEV(db.Model):
    __tablename__ = 'cmdb_DEV'
    id = db.Column('id', db.String(128), primary_key = True, nullable = False, unique = True)
    id_os = db.Column(db.String(128))
    id_part_list = db.Column(db.String(10240))
    run_time = db.Column(db.Date)
    disk = db.Column(db.String(128))
    size = db.Column(db.Integer)
    part_list = db.Column(db.String(128))
    insert_time = db.Column(db.Date)
    update_time = db.Column(db.Date)
