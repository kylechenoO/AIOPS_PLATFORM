'''
    OS.py Lib
    Written By Kyle Chen
    Version 20190318v1
'''

# import buildin pkgs
import os
import re
import sys

## OS Class
class OS(object):

    ## initial function
    def __init__(self, logger):

        self.logger = logger
        self.title = ['id', 'hardware_id', 'os_version', 'kernel', 'python_version', 'installed_pkgs', 'ipList', 'interfaceList', 'id_NETList']
        self.result = []

    ## get data
    def getData(self):
        if self.checkContainer():
            self.result = [self.title, [''] * len(self.title)]
            self.logger.debug('[OS][{}]'.format(self.result))
            return(self.result)

        hardware_id_val = self.getHardwareID()
        id_val = 'OS-{}'.format(hardware_id_val)

    ## get Hardware ID
    def getHardwareID(self):

        result = ''
        with open('/sys/devices/virtual/dmi/id/product_uuid') as fp:
            result = fp.read()

        return(result)

    ## check if there's an /.dockerenv file exist
    def checkContainer(self):
        if os.path.isfile('/.dockerenv'):
            return(True)

        else:
            return(False)
