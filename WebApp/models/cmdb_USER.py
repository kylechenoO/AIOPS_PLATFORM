'''
    cmdb_USER.py Lib
    Written By Kyle Chen
    Version 20190415v1
'''

# import buildin pkgs

## import priviate pkgs
from models.Global import db

## cmdb_USER Class
class cmdb_USER(db.Model):
    __tablename__ = 'cmdb_USER'
    id = db.Column('id', db.String(128), primary_key = True, nullable = False, unique = True)
    id_os = db.Column(db.String(128))
    id_group = db.Column(db.String(128))
    run_time = db.Column(db.Date)
    uid = db.Column(db.Integer)
    gid = db.Column(db.Integer)
    user_name = db.Column(db.String(64))
    home = db.Column(db.String(64))
    shell = db.Column(db.String(64))
    status = db.Column(db.String(8))
    insert_time = db.Column(db.Date)
    update_time = db.Column(db.Date)
