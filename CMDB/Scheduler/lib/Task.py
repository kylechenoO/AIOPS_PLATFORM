'''
    Task.py Lib
    Written By Kyle Chen
    Version 20190328v1
'''

# import buildin pkgs
import os
import re

## import priviate pkgs
from SubProc import SubProc

## Task Class
class Task(object):
    ## initial function
    def __init__(self, logger, config):
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
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
                line = re.sub(r' +', ' ', line)
                line = line.split(' ')
                min_val = line[0]
                hor_val = line[1]
                day_val = line[2]
                mon_val = line[3]
                wkd_val = line[4]
                cmd_val = line[5:]
                result.append([min_val, hor_val, day_val, mon_val, wkd_val, ' '.join(cmd_val)])

        return(result)

    ## load all tasks in all file
    def loadAllTasks(self):
        result = []
        file_list = self.scanFiles()
        for file_name in file_list:
            result += self.loadTasks(file_name)

        return(result)

    ## is Now, time check
    def isNow(self, time_list):
        self.logger.debug('[isNow][{}]'.format(time_list))
        return(True)
    ## run func
    def run(self):
        result = []
        self.logger.debug('[{}]Task Start'.format(self.name))
        task_list = self.loadAllTasks()
        for task in task_list:
            if self.isNow(task[:5]):
                procObj = SubProc(self.logger)
                cmd = task[-1]
                self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))

        self.logger.debug('[{}][{}]'.format(self.name, task_list))
        self.logger.debug('[{}]Task End'.format(self.name))
        return(result)
