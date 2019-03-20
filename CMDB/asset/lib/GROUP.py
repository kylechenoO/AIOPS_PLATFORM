'''
    GROUP.py Lib
    Written By Kyle Chen
    Version 20190320v1
'''

# import buildin pkgs
import os
import re
import dmidecode

## GROUP Class
class GROUP(object):
    ## initial function
    def __init__(self, logger, config):
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.logger = logger
        self.os_id = ''
        self.title = ['id', 'id_os', 'id_user_list', 'gid',
                        'group_name', 'user_list']
        self.result = [self.title]

    ## get data
    def getData(self):
        if self.checkContainer():
            self.result = [self.title, [''] * len(self.title)]
            self.logger.debug('[{}][{}][{}]'.format(self.name, self.name, self.result))
            return(self.result)

        self.os_id = self.getOSId()
        id_os_val = 'OS-{}'.format(self.os_id)
        self.logger.debug('[{}][id][{}]'.format(self.name, id_os_val))

        group_dict = self.getGroupInfo()
        user_dict = self.getUserInfo()

        for group_name in group_dict:
            gid_val = group_dict[group_name]['gid']
            self.logger.debug('[{}][gid][{}]'.format(self.name, gid_val))

            id_val = '{}-{}-{}'.format(self.name, self.os_id, gid_val)
            self.logger.debug('[{}][id][{}]'.format(self.name, id_val))

            group_name_val = group_name
            self.logger.debug('[{}][group_name][{}]'.format(self.name, group_name_val))

            user_list_val = self.getUserVal(user_dict, gid_val)
            self.logger.debug('[{}][user_list][{}]'.format(self.name, ','.join(user_list_val)))

            id_user_list_val = ','.join([ 'USER-{}-{}'.format(self.os_id, uid) for uid in user_list_val ])
            self.logger.debug('[{}][id_user_list][{}]'.format(self.name, id_user_list_val))

            user_list_val = ','.join(user_list_val)
            self.result.append([id_val, id_os_val, id_user_list_val, gid_val,
                                group_name_val, user_list_val])
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
    def getGroupInfo(self):
        result = {}
        with open('/etc/group', 'r') as fp:
            group_data_raw = fp.read()

        line_list = group_data_raw.split('\n')
        line_list.remove('')
        for line in line_list:
            line = line.split(':')
            result[line[0]] = {
                'gid': line[2]
            }
        
        return(result)

    ## get Shadow Info
    def getUserInfo(self):
        result = {}
        with open('/etc/passwd', 'r') as fp:
            passwd_data_raw = fp.read()

        data_line = passwd_data_raw.split('\n')
        data_line.remove('')
        for line in data_line:
            line = line.split(':')
            user_name = line[0]
            result[user_name] = {
                'uid': line[2],
                'gid': line[3]
            }

        return(result)

    ## get a user's val from user_info
    def getUserVal(self, user_dict, gid):
        result = []
        for user_name in user_dict:
            if user_dict[user_name]['gid'] == gid:
                result.append(user_dict[user_name]['uid'])

        return(result)
