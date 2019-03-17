'''
    OS.py Lib
    Written By Kyle Chen
    Version 20190317v1
'''

# import buildin pkgs
import os
import re
import sys
import subprocess

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
            self.result = { key: '' for key in self.title }
            self.logger.debug('[%s]'.format(self.result))
            return(self.result)

    ## check if there's an /.dockerenv file exist
    def checkContainer(self):
        if os.path.isfile('/.dockerenv'):
            return(True)

        else:
            return(False)
