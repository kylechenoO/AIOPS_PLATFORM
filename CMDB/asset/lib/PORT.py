'''
    PORT.py Lib
    Written By Kyle Chen
    Version 20190321v1
'''

# import buildin pkgs
import os
import re
import dmidecode
import psutil
import socket
from pwd import getpwnam 
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM

## USER Class
class PORT(object):
    ## initial function
    def __init__(self, logger, config):
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.logger = logger
        self.os_id = ''
        self.title = ['id', 'id_os', 'id_user', 'id_proc', 'id_neti_list', 'rel_port_list',
                        'type', 'listening_ip_list', 'port', 'status', 'pid',
                        'neti_list', 'user', 'uid', 'dst_ip', 'dst_port']
        self.result = [self.title]

    ## get data
    def getData(self):
        if self.checkContainer():
            self.result = [self.title, [''] * len(self.title)]
            self.logger.debug('[{}][{}][{}]'.format(self.name, self.name, self.result))
            return(self.result)

        self.os_id = self.getOSId()
        id_os_val = 'OS-{}'.format(self.os_id)
        self.logger.debug('[{}][id][{}]'.format(self.name, id_os_val))

        portinfo_list = self.getPortInfo()
        for line in portinfo_list:
            type_val, status_val, listening_ip_list_val, port_val, dst_ip_val, dst_port_val, pid_val = line
            id_val = '{}-{}-{}-{}'.format(self.name, self.os_id, type_val, port_val)
            user_val, uid_val = self.getProcInfo(pid_val)
            id_user_val = 'USER-{}-{}'.format(self.os_id, uid_val)
            id_proc_val = 'PROC-{}-{}'.format(self.os_id, pid_val)

            ## get real ip list
            ## STOPPED HERE
            listening_ip_list_val = self.getRealIP(listening_ip_list_val)

            rel_port_list_val = []
            if status_val == 'LISTEN':
                for i in listening_ip_list_val:
                    rel_port_list_val.append('REL-PORT-LISTENING-{}-{}-{}'.format(i, type_val, port_val))

            elif status_val == 'ESTABLISHED':
                rel_port_list_val.append('REL-PORT-CLIENT-{}-TCP-{}'.format(dst_ip_val, port_val))

            rel_port_list_val = ','.join(rel_port_list_val)

            neti_list_val = ''
            id_neti_list_val = ''

            self.result.append([id_val, id_os_val, id_user_val, id_proc_val, id_neti_list_val,
                                rel_port_list_val, type_val, listening_ip_list_val, port_val, status_val,
                                pid_val, neti_list_val, user_val, uid_val, dst_ip_val, dst_port_val])
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
    def getPortInfo(self):
        result = []
        AF_INET6 = getattr(socket, 'AF_INET6', object())
        type_map = {
            (AF_INET, SOCK_STREAM): 'TCP',
            (AF_INET6, SOCK_STREAM): 'TCP6',
            (AF_INET, SOCK_DGRAM): 'UDP',
            (AF_INET6, SOCK_DGRAM): 'UDP6',
        }
        netproc = psutil.net_connections()
        for n in netproc:
            pid = ''
            raddr_ip = ''
            raddr_port = ''
            type_val = type_map[(n.family, n.type)]
            laddr_ip = n.laddr[0]
            laddr_port = n.laddr[1]
            status = n.status
            pid = n.pid
            if len(n.raddr) > 0:
                raddr_ip = n.raddr[0]
                raddr_port = n.raddr[1]

            result.append([type_val, status, [laddr_ip], laddr_port, raddr_ip, raddr_port, pid])
        return(result)

    ## get Proc Info
    def getProcInfo(self, pid):
        result = ''
        p = psutil.Process(pid)
        user_name = p.username()
        uid = getpwnam(user_name).pw_uid
        result = (user_name, uid)
        return(result)

    ## get Real IP
    def getRealIP(self, ip_list):
        result = ()
        if ip_list == '127.0.0.1':
            return(ip_list)
            pass

        elif ip_list == ':::':
            return(ip_list)
            pass

        else:
            ## result(ip_list[0], self.getInterfaceList(ip_list[0]))
            return(ip_list)

        return(result)

    ## get Interface Info
    def getInterfaceList(self, ip):
        result = []
        return(result)
