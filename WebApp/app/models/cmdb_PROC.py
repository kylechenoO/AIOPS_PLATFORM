'''
    cmdb_PROC.py Lib
    Written By Kyle Chen
    Version 20190420v1
'''

# import buildin pkgs

## import priviate pkgs
from app import db

## cmdb_PROC Class
class cmdb_PROC(db.Model):
    __tablename__ = 'cmdb_PROC'
    id = db.Column('id', db.String(128), primary_key = True, nullable = False, unique = True)
    id_os = db.Column(db.String(128))
    id_user = db.Column(db.String(128))
    run_time = db.Column(db.Date)
    pid = db.Column(db.Integer)
    proc_name = db.Column(db.String(128))
    user = db.Column(db.String(16))
    status = db.Column(db.String(16))
    command = db.Column(db.Text)
    environ = db.Column(db.Text)
    insert_time = db.Column(db.Date)
    update_time = db.Column(db.Date)
