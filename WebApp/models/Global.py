'''
    Global.py Lib
    Written By Kyle Chen
    Version 20190403v1
'''

# import buildin pkgs
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

## global values
db = SQLAlchemy()
login_manager = LoginManager()
