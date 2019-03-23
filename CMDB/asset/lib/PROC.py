'''
    PROC.py Lib
    Written By Kyle Chen
    Version 20190322v1
'''

# import buildin pkgs
import os
import re
import dmidecode
import psutil

## PROC Class
class PROC(object):
    ## initial function
    def __init__(self, logger, config):
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.logger = logger
        self.os_id = ''
        self.title = ['id', 'id_os', 'id_user', 'pid', 'proc_name', 'user',
                        'status', 'command', 'environ']
        self.result = [self.title]

    ## get data
    def getData(self):
        if self.checkContainer():
            self.result = [self.title, [''] * len(self.title)]
            self.logger.debug('[{}][{}][{}]'.format(self.name, self.name, self.result))
            return(self.result)

        self.os_id = self.getOSId()
        id_os_val = 'OS-{}'.format(self.os_id)
        self.logger.debug('[{}][id_os][{}]'.format(self.name, id_os_val))
        proc_list = self.getProcList()
        for line in proc_list:
            pid_val, proc_name_val, user_name_val, status_val, command_val, environ_val  = line
            id_val = '{}-{}-{}'.format(self.name, self.os_id, pid_val)
            id_user_val = 'USER-{}-{}'.format(self.os_id, user_name_val)
            self.logger.debug('[{}][id][{}]'.format(self.name, id_val))
            self.logger.debug('[{}][id_os][{}]'.format(self.name, id_os_val))
            self.logger.debug('[{}][id_user][{}]'.format(self.name, id_user_val))
            self.logger.debug('[{}][pid][{}]'.format(self.name, pid_val))
            self.logger.debug('[{}][proc_name][{}]'.format(self.name, proc_name_val))
            self.logger.debug('[{}][user_name][{}]'.format(self.name, user_name_val))
            self.logger.debug('[{}][status][{}]'.format(self.name, status_val))
            self.logger.debug('[{}][command][{}]'.format(self.name, command_val))
            self.logger.debug('[{}][environ][{}]'.format(self.name, environ_val))
            self.result.append([id_val, id_os_val, id_user_val, pid_val, proc_name_val,
                                user_name_val, status_val, command_val, environ_val])
        return(self.result)

    ## check if there's an /.dockerenv file exist
    def checkContainer(self):
        if os.path.isfile('/.dockerenv'):
            return(True)

        else:
            return(False)

    ## get Hardware Info
    def getOSId(self):
        hardware_info = dmidecode.get_by_type(1)[0]
        hardware_id = re.sub('-', '',hardware_info['UUID'])
        result = hardware_id
        return(result)

    ## get Port Info
    def getProcList(self):
        result = []
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            e_dict = p.environ()
            e_list = []
            for e in e_dict:
                e_list.append('{}={}'.format(e, e_dict[e]))

            result.append([pid, p.name(), p.username(), p.status(), ' '.join(p.cmdline()), ' '.join(e_list)])
        return(result)
