'''
    CiConfig.py Lib
    Written By Kyle Chen
    Version 20190326v1
'''

# import buildin pkgs
import os
import re
import configparser

## CiConfig Class
class CiConfig(object):
    ## initial function
    def __init__(self, logger, workpath, ci):
        self.ci = ci
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.logger = logger
        self.workpath = workpath
        config_fp = '{}/etc/{}.conf'.format(self.workpath, ci)
        configParserObj = configparser.ConfigParser()
        configParserObj.read(config_fp)
        self.config_dict = { op: configParserObj[self.ci][op] for op in configParserObj.options(self.ci) }
        self.logger.debug('[CONF][{}]'.format(self.config_dict))
    
    ## getConfig context
    def getConfig(self, ci):
        result = {}
        self.logger.debug('[{}][{}]'.format(self.name, self.ci))
        return(result)

    ## run func
    def run(self):
        self.logger.debug('[{}]Getting Config Start'.format(self.name))
        self.getConfig(self.ci)
        self.logger.debug('[{}]Getting Config End'.format(self.name))
        return(True)
