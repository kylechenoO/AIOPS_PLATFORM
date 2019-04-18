'''
    run.py
    Written By Kyle Chen
    Version 20190418v1
'''

# import buildin pkgs
import os
import re
import sys
import logging
from time import strftime
from flask_restful import Api
from flask import Flask, request
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler

## initial workpath valus
workpath = os.path.abspath(os.path.dirname(__file__))

## import priviate pkgs
from lib.App import App
from lib.Config import Config
from pages.IndexPage import IndexPage
from pages.SignInPage import SignInPage
from pages.SignUpPage import SignUpPage
from pages.SignOutPage import SignOutPage

## load config
config = Config(workpath)
LISTEN_IP = config.SYS_LISTEN_IP
LISTEN_PORT = config.SYS_LISTEN_PORT
DEBUG = config.SYS_DEBUG
MARIADB_HOST = config.MARIADB_HOST
MARIADB_PORT = config.MARIADB_PORT
MARIADB_USER = config.MARIADB_USER
MARIADB_PASSWORD = config.MARIADB_PASSWORD
MARIADB_DATABASE = config.MARIADB_DATABASE
name = re.sub('\..*$', '', os.path.basename(__file__))

## some flask args
app = Flask(name, template_folder = 'templates', static_folder = 'static')
app.secret_key = os.urandom(24)
api = Api(app)

## initial log
@app.after_request
def after_request(response):
    if response.status_code != 500:
        ts = strftime('[%Y-%b-%d %H:%M]')
        logger.info('%s %s %s %s %s %s',
                      ts,
                      request.remote_addr,
                      request.method,
                      request.scheme,
                      request.full_path,
                      response.status)
    return(response)

@app.errorhandler(Exception)
def exceptions(e):
    """ Logging after every Exception. """
    ts = strftime('[%Y-%b-%d %H:%M]')
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR',
                  ts,
                  request.remote_addr,
                  request.method,
                  request.scheme,
                  request.full_path)
    return("Internal Server Error", 500)

try:
    log_level = getattr(logging, config.LOG_LEVEL)

except BaseException:
    log_level = logging.NOTSET

logger = logging.getLogger(name)
logger.setLevel(log_level)
formatter = logging.Formatter(
            '[%(asctime)s][%(name)s][%(levelname)s] %(message)s')
handler = RotatingFileHandler(
            config.LOG_FILE,
            mode='a',
            maxBytes=config.LOG_MAX_SIZE,
            backupCount=config.LOG_BACKUP_COUNT)
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug('WebApp Initial Start')
logger.debug('[SYS_LISTEN_IP][%s]' % (config.SYS_LISTEN_IP))
logger.debug('[SYS_LISTEN_PORT][%s]' % (config.SYS_LISTEN_PORT))
logger.debug('[SYS_DEBUG][%s]' % (config.SYS_DEBUG))
logger.debug('[LOCK_DIR][%s]' % (config.LOCK_DIR))
logger.debug('[LOCK_FILE][%s]' % (config.LOCK_FILE))
logger.debug('[LOG_DIR][%s]' % (config.LOG_DIR))
logger.debug('[LOG_FILE][%s]' % (config.LOG_FILE))
logger.debug('[LOG_LEVEL][%s]' % (config.LOG_LEVEL))
logger.debug('[LOG_MAX_SIZE][%s]' % (config.LOG_MAX_SIZE))
logger.debug(
    '[LOG_BACKUP_COUNT][%s]' %
    (config.LOG_BACKUP_COUNT))
logger.debug('WebApp Initial Done')


## init db config
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://{}:{}@{}:{}/{}'.format(MARIADB_USER, MARIADB_PASSWORD,
    MARIADB_HOST, MARIADB_PORT, MARIADB_DATABASE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy()
db.init_app(app)

## set up login manager
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'signinpage'
login_manager.login_message = 'Unauthorized User'
login_manager.login_message_category = 'info'
login_manager.init_app(app)
csrf = CSRFProtect()
csrf.init_app(app)

## set route
api.add_resource(IndexPage, '/')
api.add_resource(SignInPage, '/sign_in')
api.add_resource(SignUpPage, '/sign_up')
api.add_resource(SignOutPage, '/sign_out')

## run app
app.run(
    host = LISTEN_IP,
    port = LISTEN_PORT,
    debug = DEBUG,
    use_reloader = False
)
