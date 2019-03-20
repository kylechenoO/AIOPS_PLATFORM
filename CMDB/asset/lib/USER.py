'''
    USER.py Lib
    Written By Kyle Chen
    Version 20190320v1
'''

# import buildin pkgs
import os
import re
import dmidecode

## USER Class
class USER(object):
    ## initial function
    def __init__(self, logger, config):
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.logger = logger
        self.os_id = ''
        self.title = ['id', 'id_os', 'id_group', 'uid', 'gid', 'user_name',
                        'home', 'shell', 'status']
        self.result = []

    ## get data
    def getData(self):
        if self.checkContainer():
            self.result = [self.title, [''] * len(self.title)]
            self.logger.debug('[{}][{}]'.format(self.name, self.result))
            return(self.result)

        self.os_id = self.getOSId()
        id_os = 'OS-{}'.format(self.os_id)
        self.logger.debug('[id_os][{}]'.format(id_os))

        id_os_val = 'OS-{}'.format(self.os_id)
        self.logger.debug('[id][{}]'.format(id_os_val))

        data_list = self.getUserInfo()
        uid_val = ''
        id_val = ''

        gid_val = ''
        id_group_val = ''

        user_name_val = ''
        home_val = ''
        shell_val = ''
        status_val = ''

        self.result = [self.title, [id_val, id_os_val, id_group_val, uid_val,
                        gid_val, user_name_val, home_val, shell_val, status_val]]
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

    ## get User Info
    def getUserInfo(self):
        result = []
        with open('/etc/passwd', 'r') as fp:
            passwd_data_raw = fp.read()

        data_line = passwd_data_raw.split('\n')
        for line in data_line:
            data = line.split(':')
            user_name = data[0]
            uid = data[2]
            gid = data[3]
            home = data[5]
            shell = data[6]
            result.append([user_name, uid, gid, home, shell])
        
        return(result)

    ## get Shadow Info
    def getStatus(self):
        result = {}
        with open('/etc/shadow', 'r') as fp:
            shadow_data_raw = fp.read()

        data_line = passwd_data_raw.split('\n')
        for line in data_line:
            data = line.split(':')
            user_name = data[0]
            status = data[1]
            ## STOPPED HERE
            result[user_name] = status
        
        return(result)
