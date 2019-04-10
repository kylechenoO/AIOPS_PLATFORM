'''
    PART.py Lib
    Written By Kyle Chen
    Version 20190410v1
'''

# import buildin pkgs
import os
import re
import psutil
import dmidecode

## import priviate pkgs
from SubProc import SubProc

## PART Class
class PART(object):
    ## initial function
    def __init__(self, logger, config):
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.scripts_dir = config.SUBPROC_SCRIPTSDIR
        self.proc_timeout = config.SUBPROC_TIMEOUT
        self.logger = logger
        self.os_id = ''
        self.container_id = ''
        self.title = ['id', 'id_os', 'id_dev', 'disk', 'part', 'type', 'mounted', 'mount_point',
                        'size', 'disk_usage']
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
                    self.container_id = '-{}'.format(self.container_id)

        self.os_id = self.getOSId()
        id_os_val = 'OS-{}'.format(self.os_id)
        self.logger.debug('[{}][id_os][{}]'.format(self.name, id_os_val))
        part_dict = self.getPartInfo()
        mounted_dict = self.getMountedParts()
        swap_dict = self.getSwapParts()
        for part in part_dict:
            disk_val = part_dict[part]['disk']
            part_val = part
            size_val = part_dict[part]['size']
            type_val = ''
            mounted_val = False
            mount_point_val = ''
            disk_usage_val = ''
            if part in mounted_dict:
                type_val = mounted_dict[part]['type']
                mounted_val = True
                mount_point_val = mounted_dict[part]['mount_point']
                disk_usage_val = '{}%'.format(psutil.disk_usage(mount_point_val).percent)

            elif part in swap_dict:
                type_val = 'swap'
                mounted_val = True
                mount_point_val = 'swap'
                disk_usage_val = '{}%'.format(swap_dict[part]['usage'])

            id_val = '{}-{}-{}'.format(self.name, self.os_id, part_val)
            id_dev_val = 'DEV-{}-{}'.format(self.name, disk_val)
            self.logger.debug('[{}][id][{}]'.format(self.name, id_val))
            self.logger.debug('[{}][id_dev][{}]'.format(self.name, id_dev_val))
            self.logger.debug('[{}][disk][{}]'.format(self.name, disk_val))
            self.logger.debug('[{}][type][{}]'.format(self.name, type_val))
            self.logger.debug('[{}][mount_point][{}]'.format(self.name, mount_point_val))
            self.logger.debug('[{}][mounted][{}]'.format(self.name, mounted_val))
            self.logger.debug('[{}][size][{}]'.format(self.name, size_val))

            self.result.append([id_val, id_os_val, id_dev_val, disk_val, part_val, type_val,
                                mounted_val, mount_point_val, size_val, disk_usage_val])

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

    ## get Partition Info
    def getPartInfo(self):
        result = {}
        with open('/proc/partitions', 'r') as fp:
            data = fp.read()

        data = data.split('\n')
        data.remove('')
        exp_dev = ['name', 'sr0', '']
        disk_name = ''
        for line in data:
            disk = line.strip('\n').split(' ')[-1]
            if disk in exp_dev:
                continue

            if re.match(r'^[s,h,v]d[a-z]$', disk):
                hdisk = disk

            elif re.match(r'^[s,h,v]d[a-z][0-9]*$', disk):
                disk_size = int(int(line.strip('\n').split(' ')[-2]) / 1024 / 1024)
                result[disk] = {
                                'size': disk_size,
                                'part': disk,
                                'disk': hdisk,
                                }

        return(result)

    ## get Mounted Parts
    def getMountedParts(self):
        result = {}
        mounted_part_dict = psutil.disk_partitions()
        for part in mounted_part_dict:
            result[re.sub('^.*/', '', part.device)] = {
                                                        'mount_point': part.mountpoint,
                                                        'type': part.fstype,
                                                        'path': part.device
                                                    }

        return(result)

    ## get Swap Parts
    def getSwapParts(self):
        result = {}
        procObj = SubProc(self.logger, self.proc_timeout)
        cmd = '{}/getSwapParts.sh'.format(self.scripts_dir)
        self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
        data = procObj.run(cmd)[0].decode('utf-8')
        data = data.split('\n')
        data.remove('')
        for line in data:
            line = line.split(',')
            result[re.sub('^.*/', '', line[0])] = {
                                                    'usage': line[1],
                                                    'hdisk': line[0]
                                                }

        return(result)
