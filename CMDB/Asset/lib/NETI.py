'''
    NETI.py Lib
    Written By Kyle Chen
    Version 2019410v1
'''

# import buildin pkgs
import os
import re
import psutil
import datetime
import dmidecode
import netifaces

## NETI Class
class NETI(object):
    ## initial function
    def __init__(self, logger, config):
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.logger = logger
        self.os_id = ''
        self.container_id = ''
        self.title = ['id', 'id_os', 'run_time', 'interface', 'mac', 'ipv4_ip', 'ipv6_ip',
                        'ipv4_netmask', 'ipv6_netmask', 'default_nic',
                        'gateway', 'status']
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
        neti_list = self.getNetiInfo()
        status_dict = self.getNetiStatus()
        default_gateway_dict = self.getDefaultGateway()
        for line in neti_list:
            interface_val, ipv4_ip_val, ipv6_ip_val, ipv4_netmask_val, ipv6_netmask_val, mac_val = line
            id_val = '{}-{}-{}'.format(self.name, self.os_id, interface_val)
            default_nic_val = True if interface_val in default_gateway_dict else False
            gateway_val = default_gateway_dict[interface_val] if interface_val in default_gateway_dict else ''
            status_val = status_dict[interface_val] if interface_val in status_dict else ''
            self.logger.debug('[{}][id][{}]'.format(self.name, id_val))
            self.logger.debug('[{}][interface][{}]'.format(self.name, interface_val))
            self.logger.debug('[{}][mac][{}]'.format(self.name, mac_val))
            self.logger.debug('[{}][ipv4_ip][{}]'.format(self.name, ipv4_ip_val))
            self.logger.debug('[{}][ipv6_ip][{}]'.format(self.name, ipv6_ip_val))
            self.logger.debug('[{}][ipv4_netmask][{}]'.format(self.name, ipv4_netmask_val))
            self.logger.debug('[{}][ipv6_netmask][{}]'.format(self.name, ipv6_netmask_val))
            self.logger.debug('[{}][default_nic][{}]'.format(self.name, default_nic_val))
            self.logger.debug('[{}][gateway][{}]'.format(self.name, gateway_val))
            self.logger.debug('[{}][status][{}]'.format(self.name, status_val))
            self.result.append([id_val, id_os_val, run_time_val, interface_val, mac_val, ipv4_ip_val,
                                    ipv6_ip_val, ipv4_netmask_val, ipv6_netmask_val, default_nic_val,
                                    gateway_val, status_val])
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

    ## get Neti Info
    def getNetiInfo(self):
        result = []
        neti_dict = psutil.net_if_addrs()
        for neti in neti_dict:
            ipv4_ip = ''
            ipv6_ip = ''
            ipv4_netmask = ''
            ipv6_netmask = ''
            mac = ''

            snic_list = neti_dict[neti]
            for snic in snic_list:
                if snic.family.name == 'AF_INET':
                    ipv4_ip = snic.address
                    ipv4_netmask = snic.netmask

                elif snic.family.name == 'AF_INET6':
                    ipv6_ip = snic.address
                    ipv6_netmask = snic.netmask

                elif snic.family.name == 'AF_PACKET':
                    mac = snic.address

            result.append([neti, ipv4_ip, ipv6_ip, ipv4_netmask,
                            ipv6_netmask, mac])
        
        return(result)

    ## get Neti Status
    def getNetiStatus(self):
        result = {}
        status_dict = psutil.net_if_stats()
        for neti in status_dict:
            result[neti] = status_dict[neti].isup

        return(result)

    ## get Default GateWay
    def getDefaultGateway(self):
        result = {}
        gateway, neti = netifaces.gateways()['default'][netifaces.AF_INET]
        result[neti] = gateway

        return(result)
