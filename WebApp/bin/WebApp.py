'''
    WebApp.py
    Written By Kyle Chen
    Version 20190330v1
'''

## import buildin pkgs
import os
import re
import sys
import logging
from logging.handlers import RotatingFileHandler

## get workpath
workpath = ""
pathlst = re.split(r"\/", sys.path[0])
max_index = len(pathlst) - 1
i = 0

while i < max_index - 1:
    workpath += pathlst[i] + "/"
    i += 1

workpath += pathlst[i]

## append workpath to path
sys.path.append("%s/lib" % (workpath))
sys.path.append("%s/models" % (workpath))
sys.path.append("%s/views" % (workpath))

## import priviate pkgs
from Config import Config
from Lock import Lock
from App import App

## WebApp Class
class WebApp(object):
    ## initial function
    def __init__(self):
        ## set priviate values
        self.config = Config(workpath)
        self.pid = os.getpid()
        self.pname = 'WebApp.py'

        ## logger initial
        self.loggerInit()

        ## lock initial
        self.lockObj = Lock(
            self.pname,
            self.pid,
            self.config.LOCK_DIR,
            self.config.LOCK_FILE,
            self.logger)

        ## debug output
        self.logger.debug('WebApp Initial Start')
        self.logger.debug('[SYS_LISTEN_IP][%s]' % (self.config.SYS_LISTEN_IP))
        self.logger.debug('[SYS_LISTEN_PORT][%s]' % (self.config.SYS_LISTEN_PORT))
        self.logger.debug('[SYS_DEBUG][%s]' % (self.config.SYS_DEBUG))
        self.logger.debug('[LOCK_DIR][%s]' % (self.config.LOCK_DIR))
        self.logger.debug('[LOCK_FILE][%s]' % (self.config.LOCK_FILE))
        self.logger.debug('[LOG_DIR][%s]' % (self.config.LOG_DIR))
        self.logger.debug('[LOG_FILE][%s]' % (self.config.LOG_FILE))
        self.logger.debug('[LOG_LEVEL][%s]' % (self.config.LOG_LEVEL))
        self.logger.debug('[LOG_MAX_SIZE][%s]' % (self.config.LOG_MAX_SIZE))
        self.logger.debug(
            '[LOG_BACKUP_COUNT][%s]' %
            (self.config.LOG_BACKUP_COUNT))
        self.logger.debug('WebApp Initial Done')

    ## initial logger
    def loggerInit(self):
        self.logger = logging.getLogger("WebApp")

        try:
            log_level = getattr(logging, self.config.LOG_LEVEL)

        except BaseException:
            log_level = logging.NOTSET

        self.logger.setLevel(log_level)

        fh = RotatingFileHandler(
            self.config.LOG_FILE,
            mode='a',
            maxBytes=self.config.LOG_MAX_SIZE,
            backupCount=self.config.LOG_BACKUP_COUNT)
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
    def run(self):
        self.logger.debug('WebApp Start')

        appObj = App(self.logger, self.config)
        appObj.run()

        ## release lock
        self.lockObj.release()

        return(True)

## run it
webappObj = WebApp()
webappObj.run()
