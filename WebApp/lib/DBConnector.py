'''
    DBConnector.py
    Written By Kyle Chen
    Version 20190402v1
'''

## import buildin pkgs
import os
import re
import sys
import logging
from logging.handlers import RotatingFileHandler

## get workpath
workpath = ''
pathlst = re.split(r'\/', sys.path[0])
max_index = len(pathlst) - 1
i = 0

while i < max_index - 1:
    workpath += pathlst[i] + '/'
    i += 1

workpath += pathlst[i]

## import priviate pkgs
from Config import Config
from MariaDB import MariaDB

## DBConnector Class
class DBConnector(object):
    ## initial function
    def __init__(self):
        ## set priviate values
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        config = Config(workpath)
        self.SYS_DEBUG = config.SYS_DEBUG
        self.DB_HOST = config.MARIADB_HOST
        self.DB_PORT = config.MARIADB_PORT
        self.DB_USER = config.MARIADB_USER
        self.DB_PASSWORD = config.MARIADB_PASSWORD
        self.DB_DATABASE = config.MARIADB_DATABASE
        self.LOG_DIR = config.LOG_DIR
        self.LOG_FILE = config.DB_LOG_FILE
        self.LOG_LEVEL = config.LOG_LEVEL
        self.LOG_MAX_SIZE = config.LOG_MAX_SIZE
        self.LOG_BACKUP_COUNT = config.LOG_BACKUP_COUNT

        ## logger initial
        self.loggerInit()

        ## debug output
        self.logger.debug('DBConnector Initial Start')
        self.logger.debug('[SYS_DEBUG][%s]' % (config.SYS_DEBUG))
        self.logger.debug('[MARIADB_HOST][%s]' % (config.MARIADB_HOST))
        self.logger.debug('[MARIADB_PORT][%s]' % (config.MARIADB_PORT))
        self.logger.debug('[MARIADB_USER][%s]' % (config.MARIADB_USER))
        self.logger.debug('[MARIADB_PASSWORD][%s]' % (config.MARIADB_PASSWORD))
        self.logger.debug('[MARIADB_DATABASE][%s]' % (config.MARIADB_DATABASE))
        self.logger.debug('[LOG_DIR][%s]' % (config.LOG_DIR))
        self.logger.debug('[LOG_FILE][%s]' % (config.LOG_FILE))
        self.logger.debug('[LOG_LEVEL][%s]' % (config.LOG_LEVEL))
        self.logger.debug('[LOG_MAX_SIZE][%s]' % (config.LOG_MAX_SIZE))
        self.logger.debug(
            '[LOG_BACKUP_COUNT][%s]' %
            (config.LOG_BACKUP_COUNT))
        self.logger.debug('DBConnector Initial Done')

    ## initial logger
    def loggerInit(self):
        self.logger = logging.getLogger("DBConnector")

        try:
            log_level = getattr(logging, self.LOG_LEVEL)

        except BaseException:
            log_level = logging.NOTSET

        self.logger.setLevel(log_level)

        fh = RotatingFileHandler(
            self.LOG_FILE,
            mode='a',
            maxBytes=self.LOG_MAX_SIZE,
            backupCount=self.LOG_BACKUP_COUNT)
        fh.setLevel(log_level)

        ch = logging.StreamHandler()
        ch.setLevel(log_level)

        formatter = logging.Formatter(
            '[%(asctime)s][%(name)s][%(levelname)s] %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        return(True)

    ## run asset function
    def run(self, exec_type, SQL):
        self.logger.debug('DBConnector Start')
        self.logger.debug('[{}][{}]'.format(self.name, SQL))
        result = ''
        if exec_type == 'insert':
            mariadbObj = MariaDB(self.logger, self.DB_HOST, self.DB_PORT, self.DB_USER, self.DB_PASSWORD, self.DB_DATABASE)
            result = mariadbObj.insertDB(SQL)

        elif exec_type == 'update':
            mariadbObj = MariaDB(self.logger, self.DB_HOST, self.DB_PORT, self.DB_USER, self.DB_PASSWORD, self.DB_DATABASE)
            result = mariadbObj.updateDB(SQL)

        elif exec_type == 'select':
            mariadbObj = MariaDB(self.logger, self.DB_HOST, self.DB_PORT, self.DB_USER, self.DB_PASSWORD, self.DB_DATABASE)
            result = mariadbObj.selectDB(SQL)

        self.logger.debug('DBConnector Done')
        return(result)

