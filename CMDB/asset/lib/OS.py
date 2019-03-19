'''
    OS.py Lib
    Written By Kyle Chen
    Version 20190318v2
'''

# import buildin pkgs
import os
import re
import sys
import time
import socket
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
        self.title = ['id', 'hardware_id', 'hardware_type', 'os_type', 'os_version', 'arch',
                        'kernel', 'hostname', 'python_version', 'installed_pkgs', 'ipList',
                        'interfaceList', 'id_NETList']
        self.result = []

    ## get data
    def getData(self):
        if self.checkContainer():
            self.result = [self.title, [''] * len(self.title)]
            self.logger.debug('[{}][{}]'.format(self.name, self.result))
            return(self.result)

        ## NOT DONE YET
        hardware_info = self.getHardwareInfo()
        hardware_id_val = hardware_info[0]
        self.logger.debug('[hardware_id][{}]'.format(hardware_id_val))

        hardware_type_val = hardware_info[1]
        self.logger.debug('[hardware_type][{}]'.format(hardware_type_val))

        id_val = '{}-{}'.format(self.name, hardware_id_val)
        self.logger.debug('[id][{}]'.format(id_val))

        os_type_val = self.getOSType()
        self.logger.debug('[os_type][{}]'.format(os_type_val))

        os_version_val = self.getOSVersion()
        self.logger.debug('[os_version][{}]'.format(os_version_val))

        arch_val = self.getArch()
        self.logger.debug('[arch][{}]'.format(arch_val))

        kernel_val = self.getKernel()
        self.logger.debug('[kernel][{}]'.format(kernel_val))

        hostname_val = self.getHostname()
        self.logger.debug('[hostname][{}]'.format(hostname_val))

        python_version_val = self.getPythonVersion()
        self.logger.debug('[python_version][{}]'.format(python_version_val))

        ## 20190318 stopped here
        installed_pkgs_val = self.getInstalledPkgs()
        self.logger.debug('[installed_pkgs][{}, ...]'.format(installed_pkgs_val.decode('utf-8').split('\n')[0]))

        ipList_val = ''
        interfaceList_val = ''
        id_NETList_val = ''

        self.result = [self.title, [id_val, hardware_id_val, hardware_type_val, os_type_val,
                        os_version_val, arch_val, kernel_val, hostname_val, python_version_val,
                        installed_pkgs_val, ipList_val, interfaceList_val, id_NETList_val]]
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

        cmd = '{}/getPkgs.sh'.format(self.scripts_dir)
        self.logger.debug('[SUBPROC][{}]'.format(cmd))
        result = procObj.run(cmd)[0]

        return(result)
