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
        self.config_fp = '{}/etc/{}.conf'.format(self.workpath, ci)
    
    ## getConfig context
    def getConfig(self, fp, ci):
        configParserObj = configparser.ConfigParser()
        configParserObj.read(fp)
        ## result = { op: configParserObj[ci][op] for op in configParserObj.options(ci) }
        result = ([ op for op in configParserObj.options(ci) ], [ configParserObj[ci][op] for op in configParserObj.options(ci) ])
        self.logger.debug('[{}][{}]'.format(self.name, result))
        return(result)

    ## run func
    def run(self):
        self.logger.debug('[{}]Getting Config Start'.format(self.name))
        result = self.getConfig(self.config_fp, self.ci)
        self.logger.debug('[{}]Getting Config End'.format(self.name))
        return(result)
