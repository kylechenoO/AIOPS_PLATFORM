'''
    OS.py Lib
    Written By Kyle Chen
    Version 20190318v1
'''

# import buildin pkgs
import os
import re
import sys
import dmidecode

## OS Class
class OS(object):

    ## initial function
    def __init__(self, logger):

        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.logger = logger
        self.title = ['id', 'hardware_id', 'os_version', 'kernel', 'python_version', 'installed_pkgs', 'ipList', 'interfaceList', 'id_NETList']
        self.result = []

    ## get data
    def getData(self):
        if self.checkContainer():
            self.result = [self.title, [''] * len(self.title)]
            self.logger.debug('[{}][{}]'.format(self.name, self.result))
            return(self.result)


        ## NOT DONE YET
        hardware_id_val = self.getHardwareID()
        self.logger.debug('[hardware_id][{}]'.format(hardware_id_val))

        id_val = '{}-{}'.format(self.name, hardware_id_val)
        self.logger.debug('[id][{}]'.format(id_val))

        self.result = [self.title, id_val, hardware_id_val]
        return(self.result)

    ## get Hardware ID
    def getHardwareID(self):

        result = re.sub('-', '', dmidecode.get_by_type(1)[0]['UUID'])
        ## with open('/sys/devices/virtual/dmi/id/product_uuid') as fp:
            ## result = fp.read()

        return(result)

    ## check if there's an /.dockerenv file exist
    def checkContainer(self):
        if os.path.isfile('/.dockerenv'):
            return(True)

        else:
            return(False)
