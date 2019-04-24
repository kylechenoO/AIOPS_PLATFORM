'''
    __init__.py
    Written By Kyle Chen
    Version 20190418v1
'''

# import buildin pkgs
import os
import sys
from flask import Flask
from flask_restful import Api
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

## initial workpath valus
workpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append('%s' % (workpath))

## import priviate pkgs
from lib.Config import Config

## load config
config = Config(workpath)
MARIADB_HOST = config.MARIADB_HOST
MARIADB_PORT = config.MARIADB_PORT
MARIADB_USER = config.MARIADB_USER
MARIADB_PASSWORD = config.MARIADB_PASSWORD
MARIADB_DATABASE = config.MARIADB_DATABASE

## initial some global values
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
admin = Admin()

## getApp func
def getApp(name):
    ## init flask
    app = Flask(name, template_folder = '{}/app/templates'.format(workpath), static_folder = '{}/app/static'.format(workpath))
    app.secret_key = os.urandom(24)
    api = Api(app)

    ## init db config
    app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://{}:{}@{}:{}/{}'.format(MARIADB_USER, MARIADB_PASSWORD,
        MARIADB_HOST, MARIADB_PORT, MARIADB_DATABASE)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    ## init admin config
    admin.init_app(app)

    ## set up login manager
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'signinpage'
    login_manager.login_message = 'Unauthorized User'
    login_manager.login_message_category = 'info'
    login_manager.init_app(app)

    ## set up csrf
    csrf.init_app(app)

    return(app, api)
