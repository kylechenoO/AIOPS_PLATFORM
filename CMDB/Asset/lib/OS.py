'''
    OS.py Lib
    Written By Kyle Chen
    Version 20190410v1
'''

# import buildin pkgs
import os
import re
import sys
import time
import psutil
import socket
import datetime
import platform
import dmidecode

## import priviate pkgs
from SubProc import SubProc

## OS Class
class OS(object):
    ## initial function
    def __init__(self, logger, config):
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.logger = logger
        self.scripts_dir = config.SUBPROC_SCRIPTSDIR
        self.proc_timeout = config.SUBPROC_TIMEOUT
        self.os_id = ''
        self.container_id = ''
        self.title = ['id', 'id_net_list', 'run_time', 'hardware_id', 'hardware_type', 'os_type', 'os_version', 'arch',
                        'kernel', 'hostname', 'python_version', 'installed_pkgs', 'ip_list',
                        'interface_list']
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

        hardware_info = self.getHardwareInfo()
        hardware_id_val = hardware_info[0]
        self.os_id = '{}{}'.format(hardware_id_val, self.container_id)
        self.logger.debug('[{}][hardware_id][{}]'.format(self.name, hardware_id_val))
        run_time_val = datetime.datetime.now()
        run_time_val = run_time_val.strftime("%Y-%m-%d %H:%M:%S")
        hardware_type_val = hardware_info[1]
        self.logger.debug('[{}][hardware_type][{}]'.format(self.name, hardware_type_val))
        id_val = '{}-{}'.format(self.name, self.os_id)
        self.logger.debug('[{}][id][{}]'.format(self.name, id_val))
        os_type_val = self.getOSType()
        self.logger.debug('[{}][os_type][{}]'.format(self.name, os_type_val))
        os_version_val = self.getOSVersion()
        self.logger.debug('[{}][os_version][{}]'.format(self.name, os_version_val))
        arch_val = self.getArch()
        self.logger.debug('[{}][arch][{}]'.format(self.name, arch_val))
        kernel_val = self.getKernel()
        self.logger.debug('[{}][kernel][{}]'.format(self.name, kernel_val))
        hostname_val = self.getHostname()
        self.logger.debug('[{}][hostname][{}]'.format(self.name, hostname_val))
        python_version_val = self.getPythonVersion()
        self.logger.debug('[{}][python_version][{}]'.format(self.name, python_version_val))
        installed_pkgs_val = re.sub('\n', ',',self.getInstalledPkgs().decode('utf-8'))
        self.logger.debug('[{}][installed_pkgs][{}, ...]'.format(self.name, installed_pkgs_val.split(',')[0]))
        network_info_list = self.getNetiAddrInfo()
        interface_list_val = network_info_list[0]
        self.logger.debug('[{}][interface_list][{}]'.format(self.name, interface_list_val))
        ip_list_val = network_info_list[1]
        self.logger.debug('[{}][ip_list][{}]'.format(self.name, ip_list_val))
        id_neti_list_val = network_info_list[2]
        self.logger.debug('[{}][id_neti_list][{}]'.format(self.name, id_neti_list_val))
        self.result.append([id_val, id_neti_list_val, run_time_val, hardware_id_val, hardware_type_val, os_type_val,
                            os_version_val, arch_val, kernel_val, hostname_val, python_version_val,
                            installed_pkgs_val, ip_list_val, interface_list_val])
        return(self.result)

    ## check if there's an /.dockerenv file exist
    def checkContainer(self):
        if os.path.isfile('/.dockerenv'):
            return(True)

        else:
            return(False)

    ## get Hardware Info
    def getHardwareInfo(self):
        ## onely run once dmidecode to get all info
        hardware_info = dmidecode.get_by_type(1)[0]
        hardware_id = re.sub('-', '',hardware_info['UUID'])
        hardware_type = hardware_info['Product Name']
        result = [hardware_id, hardware_type]
        return(result)

    ## get os_type
    def getOSType(self):
        result = platform.system()
        return(result)

    ## get os_version
    def getOSVersion(self):
        result = re.sub('-.*$', '', re.sub('^.*with-', '', platform.platform()))
        return(result)

    ## get arch
    def getArch(self):
        result = platform.processor()
        return(result)

    ## get kernel
    def getKernel(self):
        result = platform.release()
        return(result)

    ## get hostname
    def getHostname(self):
        result = socket.getfqdn()
        return(result)

    ## get python version
    def getPythonVersion(self):
        result = platform.python_version()
        return(result)

    ## get installed pkgs
    def getInstalledPkgs(self):
        result = None
        procObj = SubProc(self.logger, self.proc_timeout)
        cmd = '{}/getAllInstalledPkgs.sh'.format(self.scripts_dir)
        self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
        result = procObj.run(cmd)[0]
        return(result)

    ## get NetworkInfoList
    def getNetiAddrInfo(self):
        neti_list = []
        ipv4_list = []
        ipv6_list = []
        id_neti_list = []
        result_list = []
        neti_dict = psutil.net_if_addrs()
        for neti in neti_dict:
            neti_list.append(neti)
            id_neti_list.append('NETI-{}-{}'.format(self.os_id, neti))
            snic_list = neti_dict[neti]
            for snic in snic_list:
                if snic.family.name == 'AF_INET':
                    ipv4_list.append(snic.address)

                elif snic.family.name == 'AF_INET6':
                    ipv6_list.append(snic.address)

        result = [','.join(neti_list), ','.join(ipv4_list + ipv6_list), ','.join(id_neti_list)]
        return(result)
