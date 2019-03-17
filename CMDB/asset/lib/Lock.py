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
        self.pname = '.*python.* %s' % (pname)
        self.lock_init(lock_dir, lock_file)

        lock_save = str(self.lock_read(lock_file))
        if (self.lock_get_process(self.pname, pid)) \
                or (lock_save != '' and self.lock_check_pid(lock_save)):
            logger.error('[%s][Already Running][%s]' % (pname, pid))
            sys.exit(-1)

        else:
            self.lock_write(lock_file, pid)

    ## initial lock
    def lock_init(self, lock_dir, lock_file):

        lock_dir = os.path.dirname(lock_file)
        if not os.path.isdir(lock_dir):
            try:
                os.mkdir(lock_dir)

            except Exception as e:
                self.logger('[%s]' % (e))
                return(False)

        if not os.path.isfile(lock_file):
            try:
                fp = open(lock_file, 'w')

            except Exception as e:
                self.logger('[%s]' % (e))
                return(False)

            fp.close()

        return(True)

    ## read lock
    def lock_read(self, lock_file):

        try:
            fp = open(lock_file, 'r')

        except Exception as e:
            self.logger('[%s]' % (e))

        lock_cont = fp.read()
        fp.close()

        return(lock_cont)

    ## write lock
    def lock_write(self, lock_file, PID):

        try:
            fp = open(lock_file, 'w')

        except Exception as e:
            self.logger('[%s]' % (e))

        fp.write(str(PID))
        fp.close()

        return(True)

    ## lock release
    def lock_release(self, lock_file):

        try:
            fp = open(lock_file, 'w')

        except Exception as e:
            self.logger('[%s]' % (e))

        fp.write('')
        fp.close()

        return(True)

    ## lock check pid
    def lock_check_pid(self, PID):

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
    def lock_get_process(self, pname, pid):

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
