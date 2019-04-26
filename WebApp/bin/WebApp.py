'''
    WebApp.py
    Written By Kyle Chen
    Version 20190424v1
'''

# import buildin pkgs
import os
import re
import sys
import logging
from time import strftime
from flask import request
from logging.handlers import RotatingFileHandler

## initial workpath valus
workpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append('%s' % (workpath))

## import priviate pkgs
from app import getApp, config, db
from app.pages.IndexPage import IndexPage
from app.pages.SignInPage import SignInPage
from app.pages.SignUpPage import SignUpPage
from app.pages.SignOutPage import SignOutPage
from app.pages.IndexPieChart1 import IndexPieChart1
from app.pages.IndexBarChart1 import IndexBarChart1
from app.pages.AssetRelChart1 import AssetRelChart1
from app.pages.AssetRelChart2 import AssetRelChart2

## get config
LISTEN_IP = config.SYS_LISTEN_IP
LISTEN_PORT = config.SYS_LISTEN_PORT
DEBUG = config.SYS_DEBUG
name = re.sub('\..*$', '', os.path.basename(__file__))

## some flask args
app, api = getApp(name)

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
logger.debug('[LOG_DIR][%s]' % (config.LOG_DIR))
logger.debug('[LOG_FILE][%s]' % (config.LOG_FILE))
logger.debug('[LOG_LEVEL][%s]' % (config.LOG_LEVEL))
logger.debug('[LOG_MAX_SIZE][%s]' % (config.LOG_MAX_SIZE))
logger.debug(
    '[LOG_BACKUP_COUNT][%s]' %
    (config.LOG_BACKUP_COUNT))
logger.debug('WebApp Initial Done')

## set route
api.add_resource(IndexPage, '/')
api.add_resource(SignInPage, '/sign_in')
api.add_resource(SignUpPage, '/sign_up')
api.add_resource(SignOutPage, '/sign_out')
api.add_resource(IndexPieChart1, '/index_pie_chart1')
api.add_resource(IndexBarChart1, '/index_bar_chart1')
api.add_resource(AssetRelChart1, '/asset_rel_chart1')
api.add_resource(AssetRelChart2, '/asset_rel_chart2')

## run app
app.run(
    host = LISTEN_IP,
    port = LISTEN_PORT,
    debug = DEBUG
)
