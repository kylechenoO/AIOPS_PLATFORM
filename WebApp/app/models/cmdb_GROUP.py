'''
    cmdb_GROUP.py Lib
    Written By Kyle Chen
    Version 20190420v1
'''

# import buildin pkgs

## import priviate pkgs
from app import db

## cmdb_GROUP Class
class cmdb_GROUP(db.Model):
    __tablename__ = 'cmdb_GROUP'
    id = db.Column('id', db.String(128), primary_key = True, nullable = False, unique = True)
    id_os = db.Column(db.String(128))
    id_user_list = db.Column(db.String(1024))
    run_time = db.Column(db.Date)
    gid = db.Column(db.Integer)
    group_name = db.Column(db.String(64))
    user_list = db.Column(db.String(512))
    insert_time = db.Column(db.Date)
    update_time = db.Column(db.Date)
