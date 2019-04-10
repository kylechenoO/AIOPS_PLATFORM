'''
    DEV.py Lib
    Written By Kyle Chen
    Version 20190410v1
'''

# import buildin pkgs
import os
import re
import psutil
import dmidecode

## DEV Class
class DEV(object):
    ## initial function
    def __init__(self, logger, config):
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.logger = logger
        self.os_id = ''
        self.container_id = ''
        self.title = ['id', 'id_os', 'id_part_list', 'disk', 'size', 'part_list']
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
        dev_dict = self.getDevInfo()
        for dev in dev_dict:
            disk_val = dev
            size_val = dev_dict[dev]['size']
            part_list_val = dev_dict[dev]['part']
            id_val = '{}-{}-{}'.format(self.name, self.os_id, disk_val)
            id_part_list_val = [ 'PART-{}-{}'.format(self.os_id, p) for p in part_list_val ]
            id_part_list_val = ','.join(id_part_list_val)
            part_list_val = ','.join(part_list_val)

            self.logger.debug('[{}][id][{}]'.format(self.name, id_val))
            self.logger.debug('[{}][part_list][{}]'.format(self.name, id_part_list_val))
            self.logger.debug('[{}][disk][{}]'.format(self.name, disk_val))
            self.logger.debug('[{}][disk_size][{}]'.format(self.name, size_val))
            self.logger.debug('[{}][part_list][{}]'.format(self.name, part_list_val))
            self.result.append([id_val, id_os_val, id_part_list_val, disk_val, size_val, part_list_val])

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

    ## get Device List
    def getDevInfo(self):
        result = {}
        with open('/proc/partitions', 'r') as fp:
            data = fp.read()

        data = data.split('\n')
        data.remove('')
        exp_dev = ['name', 'sr0', '']
        for line in data:
            disk = line.strip('\n').split(' ')[-1]
            if disk in exp_dev:
                continue

            if re.match(r'^[s,h,v]d[a-z]$', disk):
                disk_size = int(int(line.strip('\n').split(' ')[-2]) / 1024 / 1024)
                result[disk] = {
                                        'size': disk_size,
                                        'part': []
                                    }

            elif re.match(r'^[s,h,v]d[a-z][0-9]*$', disk):
                result[re.sub('[0-9]*$', '', disk)]['part'].append(disk)

        return(result)
