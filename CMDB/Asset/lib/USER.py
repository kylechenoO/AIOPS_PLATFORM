'''
    USER.py Lib
    Written By Kyle Chen
    Version 20190410v1
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
        self.container_id = ''
        self.title = ['id', 'id_os', 'id_group', 'uid', 'gid', 'user_name',
                        'home', 'shell', 'status']
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

        user_dict = self.getUserInfo()
        status_dict = self.getStatus()

        for user_name in user_dict:
            uid_val = user_dict[user_name]['uid']
            self.logger.debug('[{}][uid][{}]'.format(self.name, uid_val))

            id_val = '{}-{}-{}'.format(self.name, self.os_id, uid_val)
            self.logger.debug('[{}][id][{}]'.format(self.name, id_val))

            gid_val = user_dict[user_name]['gid']
            self.logger.debug('[{}][gid][{}]'.format(self.name, gid_val))

            id_group_val = 'GROUP-{}-{}'.format(self.os_id, gid_val)
            self.logger.debug('[{}][id_group][{}]'.format(self.name, id_group_val))

            user_name_val = user_name
            self.logger.debug('[{}][user_name][{}]'.format(self.name, user_name_val))

            home_val = user_dict[user_name]['home']
            self.logger.debug('[{}][home][{}]'.format(self.name, home_val))

            shell_val = user_dict[user_name]['shell']
            self.logger.debug('[{}][shell][{}]'.format(self.name, shell_val))

            status_val = status_dict[user_name]
            self.logger.debug('[{}][status][{}]'.format(self.name, status_val))

            self.result.append([id_val, id_os_val, id_group_val, uid_val,
                                gid_val, user_name_val, home_val, shell_val, status_val])
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

    ## get User Info
    def getUserInfo(self):
        result = {}
        with open('/etc/passwd', 'r') as fp:
            passwd_data_raw = fp.read()

        line_list = passwd_data_raw.split('\n')
        line_list.remove('')
        for line in line_list:
            line = line.split(':')
            result[line[0]] = {
                'uid': line[2],
                'gid': line[3],
                'home': line[5],
                'shell': line[6]
            }
        
        return(result)

    ## get Shadow Info
    def getStatus(self):
        result = {}
        with open('/etc/shadow', 'r') as fp:
            shadow_data_raw = fp.read()

        data_line = shadow_data_raw.split('\n')
        data_line.remove('')
        for line in data_line:
            line = line.split(':')
            user_name = line[0]
            status = line[1]
            if status != '*' and status != '!!':
                status = 'Active'

            else:
                status = 'InActive'

            result[user_name] = status
        return(result)
