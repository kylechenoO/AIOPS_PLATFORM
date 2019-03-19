'''
    Proc.py Lib
    Written By Kyle Chen
    Version 20190319v1
'''

# import buildin pkgs
import time
from subprocess import Popen, PIPE

## OS Class
class Proc(object):

    ## initial function
    def __init__(self, logger, proc_timeout):
        self.logger = logger
        self.timeout = proc_timeout

    ## run cmd func
    def run(self, cmd):
        proc = Popen(cmd.split(' '), stdout = PIPE, stderr = PIPE)
        for t in range(self.timeout):
            time.sleep(1)
            if proc.poll() is not None:
                return(proc.communicate())

        proc.kill()
        return('TIMEOUT')
