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
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM

## USER Class
class PORT(object):
    ## initial function
    def __init__(self, logger, config):
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.logger = logger
        self.os_id = ''
        self.title = ['id', 'id_os', 'id_user', 'id_proc_list', 'id_neti_list', 'rel_port_list',
                        'type', 'listening_ip_list', 'port', 'status', 'pid_list',
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

        id_user_val = ''
        id_proc_list_val = ''
        id_neti_list_val = ''
        rel_port_list_val = ''
        neti_list_val = ''
        user_val = ''
        uid_val = ''

        portinfo_list = self.getPortInfo()
        for line in portinfo_list:
            type_val, status_val, listening_ip_list_val, port_val, dst_ip_val, dst_port_val, pid_list_val = line
            id_val = '{}-{}-{}-{}'.format(self.name, self.os_id, type_val, port_val)

            ## STOPPED HERE

            self.result.append([id_val, id_os_val, id_user_val, id_proc_list_val, id_neti_list_val,
                                rel_port_list_val, type_val, listening_ip_list_val, port_val, status_val,
                                pid_list_val, neti_list_val, user_val, uid_val, dst_ip_val, dst_port_val])
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

            result.append([type_val, status, laddr_ip, laddr_port, raddr_ip, laddr_port, pid])
        return(result)
