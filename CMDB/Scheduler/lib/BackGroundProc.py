'''
    BackGroundProc.py Lib
    Written By Kyle Chen
    Version 20190328v1
'''

# import buildin pkgs
import os
import re
from subprocess import Popen, PIPE

## BackGroundProc Class
class BackGroundProc(object):
    ## initial function
    def __init__(self, logger):
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.logger = logger

    ## run cmd func
    def run(self, cmd):
        self.logger.debug('[{}][{}]'.format(self.name, cmd))
        cmd = re.sub(r"\"", "\\\"", cmd)
        proc = Popen(cmd, stdout = PIPE, stderr = PIPE, shell = True)
        result = proc.pid
        return(result)
