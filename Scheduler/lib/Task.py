'''
    Task.py Lib
    Written By Kyle Chen
    Version 20190328v2
'''

# import buildin pkgs
import os
import re
import cronex
import time

## import priviate pkgs
from BackGroundProc import BackGroundProc

## Task Class
class Task(object):
    ## initial function
    def __init__(self, logger, config):
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.now = time.gmtime(time.time())[:5]
        self.logger = logger
        self.cfg_dir = config.SYS_CFG_DIR

    ## scan all files under cfg_dir
    def scanFiles(self):
        result = []
        for file_name in os.listdir(self.cfg_dir):
            result.append(file_name)

        return(result)

    ## load all tasks in one file
    def loadTasks(self, file_name):
        result = []
        real_file = '{}/{}'.format(self.cfg_dir, file_name)
        with open(real_file) as fp:
            data = fp.read().split('\n')
            data.remove('')
            for line in data:
                result.append(cronex.CronExpression(line.strip()))

        return(result)

    ## load all tasks in all file
    def loadAllTasks(self):
        result = []
        file_list = self.scanFiles()
        for file_name in file_list:
            result += self.loadTasks(file_name)

        return(result)

    ## is Now, time check
    def isNow(self, task):
        self.logger.debug('[now][{}]'.format(self.now))
        result = task.check_trigger(time.gmtime(time.time())[:5], utc_offset=+8)
        self.logger.debug('[isNow][{}]'.format(result))
        return(result)

    ## run func
    def run(self):
        result = []
        self.logger.debug('[{}]Task Start'.format(self.name))
        task_list = self.loadAllTasks()
        for task in task_list:
            if self.isNow(task):
                cmd = task.comment
                procObj = BackGroundProc(self.logger)
                procObj.run(cmd)

        self.logger.debug('[{}][{}]'.format(self.name, task_list))
        self.logger.debug('[{}]Task End'.format(self.name))
        return(result)
