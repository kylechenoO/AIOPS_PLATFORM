'''
    cmdb_NETI.py Lib
    Written By Kyle Chen
    Version 20190415v1
'''

# import buildin pkgs

## import priviate pkgs
from models.Global import db

## cmdb_NETI Class
class cmdb_NETI(db.Model):
    __tablename__ = 'cmdb_NETI'
    id = db.Column('id', db.String(128), primary_key = True, nullable = False, unique = True)
    run_time = db.Column(db.Date)
    interface = db.Column(db.String(32))
    mac = db.Column(db.String(32))
    ipv4_ip = db.Column(db.String(32))
    ipv6_ip = db.Column(db.String(32))
    ipv4_netmask = db.Column(db.String(32))
    ipv6_netmask = db.Column(db.String(128))
    default_nic = db.Column(db.String(16))
    gateway = db.Column(db.String(32))
    status = db.Column(db.String(8))
    insert_time = db.Column(db.Date)
    update_time = db.Column(db.Date)
