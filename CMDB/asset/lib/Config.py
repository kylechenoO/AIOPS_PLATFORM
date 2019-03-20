'''
    Config module
    Read Configs From etc/global.conf
    Written By Kyle Chen
    Version 20190320v1
'''

# import buildin pkgs
import os
import re
import sys
import configparser

## Config Class
class Config(object):

    ## initial function
    def __init__(self, workpath):

        ## get workpath
        self.workpath = workpath

        ## set config file point
        global_filepath = '%s/etc/global.conf' % (self.workpath)
        configParserObj = configparser.ConfigParser()
        configParserObj.read(global_filepath)

        ## initial config vars
        self.SYS_CIS = configParserObj.get('SYS', 'CIS').split(',')
        self.SYS_SAVE_CSV = bool(configParserObj.get('SYS', 'SAVE_CSV'))
        self.SYS_CSV_DIR = configParserObj.get('SYS', 'CSV_DIR')
        self.SYS_CSV_DIR = '%s/%s' % (self.workpath, self.SYS_CSV_DIR)
        self.SUBPROC_SCRIPTSDIR = configParserObj.get('SUBPROC', 'SCRIPTSDIR')
        self.SUBPROC_SCRIPTSDIR = '%s/%s' % (self.workpath, self.SUBPROC_SCRIPTSDIR)
        self.SUBPROC_TIMEOUT = int(
            configParserObj.get(
                'SUBPROC', 'TIMEOUT'))
        self.LOCK_DIR = configParserObj.get('LOCK', 'LOCK_DIR')
        self.LOCK_DIR = '%s/%s' % (self.workpath, self.LOCK_DIR)
        self.LOCK_FILE = configParserObj.get('LOCK', 'LOCK_FILE')
        self.LOCK_FILE = '%s/%s' % (self.LOCK_DIR, self.LOCK_FILE)
        self.LOG_DIR = configParserObj.get('LOG', 'LOG_DIR')
        self.LOG_DIR = '%s/%s' % (self.workpath, self.LOG_DIR)
        self.LOG_FILE = configParserObj.get('LOG', 'LOG_FILE')
        self.LOG_FILE = '%s/%s' % (self.LOG_DIR, self.LOG_FILE)
        self.LOG_LEVEL = configParserObj.get('LOG', 'LOG_LEVEL').upper()
        self.LOG_MAX_SIZE = int(
            configParserObj.get(
                'LOG', 'LOG_MAX_SIZE')) * 1024 * 1024
        self.LOG_BACKUP_COUNT = int(
            configParserObj.get(
                'LOG', 'LOG_BACKUP_COUNT'))

        ## initial dirs
        self.dirInit(self.LOCK_DIR)
        self.dirInit(self.LOG_DIR)
        self.dirInit(self.SYS_CSV_DIR)

    ## directory initial function
    def dirInit(self, dir):

        if not os.path.exists(dir):
            try:
                os.mkdir(dir)

            except Except as e:
                sys.stderr.write('[Error][%s]' % (e))
                sys.stderr.flush()

        return(True)
