'''
    Scheduler.py
    Written By Kyle Chen
    Version 20190410v1
'''

## import buildin pkgs
import sys
import re
import os
import logging
from logging.handlers import RotatingFileHandler

## get workpath
workpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

## append workpath to path
sys.path.append("%s/lib" % (workpath))

## import priviate pkgs
from Config import Config
from Lock import Lock
from Task import Task

## Scheduler Class
class Scheduler(object):
    ## initial function
    def __init__(self):
        ## set priviate values
        self.config = Config(workpath)
        self.pid = os.getpid()
        self.pname = 'Scheduler.py'

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
        self.logger.debug('Scheduler Initial Start')
        self.logger.debug('[SYS_CFG_DIR][%s]' % (self.config.SYS_CFG_DIR))
        self.logger.debug('[LOCK_DIR][%s]' % (self.config.LOCK_DIR))
        self.logger.debug('[LOCK_FILE][%s]' % (self.config.LOCK_FILE))
        self.logger.debug('[LOG_DIR][%s]' % (self.config.LOG_DIR))
        self.logger.debug('[LOG_FILE][%s]' % (self.config.LOG_FILE))
        self.logger.debug('[LOG_LEVEL][%s]' % (self.config.LOG_LEVEL))
        self.logger.debug('[LOG_MAX_SIZE][%s]' % (self.config.LOG_MAX_SIZE))
        self.logger.debug(
            '[LOG_BACKUP_COUNT][%s]' %
            (self.config.LOG_BACKUP_COUNT))
        self.logger.debug('Scheduler Initial Done')

    ## initial logger
    def loggerInit(self):
        self.logger = logging.getLogger("Scheduler")

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
        self.logger.debug('Scheduler Start')

        ## load and run tasks
        taskObj = Task(self.logger, self.config)
        taskObj.run()

        ## release lock
        self.lockObj.release()

        return(True)

## run it
schedulerObj = Scheduler()
schedulerObj.run()
