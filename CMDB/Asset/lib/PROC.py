'''
    PROC.py Lib
    Written By Kyle Chen
    Version 20190410v1
'''

# import buildin pkgs
import os
import re
import psutil
import socket
import datetime
import dmidecode
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM

## PROC Class
class PROC(object):
    ## initial function
    def __init__(self, logger, config):
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.logger = logger
        self.os_id = ''
        self.container_id = ''
        self.title = ['id', 'id_os', 'id_user', 'run_time', 'pid', 'proc_name', 'user',
                        'status', 'command', 'environ']
        self.result = [self.title]

    ## get data
    def getData(self):
        if self.checkContainer():
            file_name = '/proc/self/cgroup'
            with open(file_name) as fp:
                data = fp.read()

            data = data.split('\n')
            data.remove('')
            for line in data:
                if line.find('cpu:/') > -1:
                    self.container_id = re.sub(r'^.*/', '', line)
                    self.container_id = '-{}'.format(self.container_id[:12])

        self.os_id = self.getOSId()
        id_os_val = 'OS-{}'.format(self.os_id)
        self.logger.debug('[{}][id_os][{}]'.format(self.name, id_os_val))
        run_time_val = datetime.datetime.now()
        run_time_val = run_time_val.strftime("%Y-%m-%d %H:%M:%S")
        proc_list = self.getProcList()
        proc_info_list = self.getProcInfoList(proc_list)
        for line in proc_info_list:
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
            self.result.append([id_val, id_os_val, id_user_val, run_time_val, pid_val, proc_name_val,
                                user_name_val, status_val, command_val, re.sub('\|', '', environ_val)])
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
        result = '{}{}'.format(hardware_id, self.container_id)
        return(result)

    ## get Proc List
    def getProcList(self):
        result = []
        netproc = psutil.net_connections()
        for n in netproc:
            pid = n.pid
            if len(n.raddr) > 0:
                raddr_ip = n.raddr[0]
                raddr_port = n.raddr[1]

            if pid is None:
                continue
            result.append(pid)
        return(result)

    ## get Port Info
    def getProcInfoList(self, proc_list):
        result = []
        for pid in proc_list:
            p = psutil.Process(pid)
            e_dict = p.environ()
            e_list = []
            for e in e_dict:
                e_list.append('{}={}'.format(e, e_dict[e]))

            result.append([pid, p.name(), p.username(), p.status(), ' '.join(p.cmdline()), ' '.join(e_list)])
        return(result)
