'''
    SubProc.py Lib
    Written By Kyle Chen
    Version 20190319v1
'''

# import buildin pkgs
import time
from subprocess import Popen, PIPE

## SubProc Class
class SubProc(object):
    ## initial function
    def __init__(self, logger):
        self.logger = logger

    ## run cmd func
    def run(self, cmd):
        proc = Popen(cmd.split(' '), stdout = PIPE, stderr = PIPE)
        return(proc)
