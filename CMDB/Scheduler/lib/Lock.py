'''
    Lock.py Lib
    Written By Kyle Chen
    Version 20190316v1
'''

# import buildin pkgs
import os
import re
import sys
import subprocess

## Lock Class
class Lock(object):
    ## initial function
    def __init__(self, pname, pid,
                 lock_dir, lock_file, logger):
        self.logger = logger
        self.logger.debug('Lock Initial Start')
        self.lock_dir = lock_dir
        self.lock_file = lock_file

        self.pname = '.*python.* %s' % (pname)
        self.init()

        lock_save = str(self.read())
        if (self.getProcess(self.pname, pid)) \
                or (lock_save != '' and self.checkPID(lock_save)):
            self.logger.error('[%s][Already Running][%s]' % (pname, pid))
            sys.exit(-1)

        else:
            self.write(pid)

        self.logger.debug('Lock Initial End')

    ## initial lock
    def init(self):
        self.lock_dir = os.path.dirname(self.lock_file)
        if not os.path.isdir(self.lock_dir):
            try:
                os.mkdir(self.lock_dir)

            except Exception as e:
                self.logger('[%s]' % (e))
                return(False)

        if not os.path.isfile(self.lock_file):
            try:
                fp = open(self.lock_file, 'w')

            except Exception as e:
                self.logger('[%s]' % (e))
                return(False)

            fp.close()

        return(True)

    ## read lock
    def read(self):
        try:
            fp = open(self.lock_file, 'r')

        except Exception as e:
            self.logger('[%s]' % (e))
            return(False)

        lock_cont = fp.read()
        fp.close()

        return(lock_cont)

    ## write lock
    def write(self, PID):
        try:
            fp = open(self.lock_file, 'w')

        except Exception as e:
            self.logger('[%s]' % (e))
            return(False)

        fp.write(str(PID))
        fp.close()

        return(True)

    ## lock check pid
    def checkPID(self, PID):
        Flag = False
        cmd = "ps -elf"
        pslst = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, shell=True)
        output = pslst.stdout.read()
        pattern = re.compile('(\ *%s \ *)' % PID)

        for line in re.finditer(pattern, str(output)):
            Flag = True
            break

        return(Flag)

    ## lock check process
    def getProcess(self, pname, pid):
        Flag = False
        cmd = "ps -elf"
        pslst = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, shell=True)
        output = pslst.stdout.read()
        pattern = re.compile(r'(%s)' % pname)

        for line in re.finditer(pattern, str(output)):

            if str(pid) not in str(line.group()):
                Flag = True

            break

        return(Flag)

    ## lock release
    ## def lock_release(self, lock_file):
    def release(self):
        self.logger.debug('Lock Release Start')
        try:
            fp = open(self.lock_file, 'w')

        except Exception as e:
            self.logger.debug('Lock Release Error')
            return(False)

        fp.write('')
        fp.close()
        self.logger.debug('Lock Release Done')

        return(True)

