'''
    DOCKER.py Lib
    Written By Kyle Chen
    Version 20190411v2
'''

# import buildin pkgs
import os
import re
import docker
import dmidecode

## import priviate pkgs
from SubProc import SubProc

## DOCKER Class
class DOCKER(object):
    ## initial function
    def __init__(self, logger, config):
        self.name = re.sub('\..*$', '', os.path.basename(__file__))
        self.logger = logger
        self.cmdb_path = os.path.dirname(config.workpath)
        self.scripts_dir = config.SUBPROC_SCRIPTSDIR
        self.proc_timeout = config.SUBPROC_TIMEOUT
        self.os_id = ''
        self.container_id = ''
        self.title = ['id', 'id_os', 'container_id', 'container_name', 'image_name', 'stats', 'status', 'port_dict', 'network_setting_dict', 'disk_dict']
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
        try:
            dockerObj = docker.from_env()

        except Exception as e:
            self.result = [self.title, [''] * len(self.title)]
            return(self.result)

        container_list = dockerObj.containers()
        for line in container_list:
            container_id_val = line['Id'][:12]
            id_val = 'OS-{}-{}'.format(self.os_id, container_id_val)
            container_name_val = re.sub('^/', '', line['Names'][0])
            image_name_val = line['Image']
            stats_val = line['State']
            status_val = line['Status']
            port_dict_val = line['Ports']
            network_setting_dict_val = line['NetworkSettings']
            disk_dict_val = line['Mounts']
            self.result.append([id_val, id_os_val, container_id_val, container_name_val, image_name_val,
                stats_val, status_val, port_dict_val, network_setting_dict_val, disk_dict_val])

            ## push Scheduler, Asset scripts to container
            ## NOT DONE YET
            if stats_val == 'running':
                procObj = SubProc(self.logger, self.proc_timeout)
                ## cmd = 'cat {}/containerCreateDirectory.sh | docker exec -i bash'.format(self.scripts_dir, container_name_val)
                cmd = 'bash {}/containerInitial.sh {} {}'.format(self.scripts_dir, self.scripts_dir, container_name_val)
                self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
                self.logger.debug('[{}][SUBPROC][{}][{}]'.format(self.name, cmd, procObj.run(cmd)[0]))

                cmd = 'docker cp {}/Scheduler {}:/AIOPS'.format(self.cmdb_path, container_name_val)
                self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
                self.logger.debug('[{}][SUBPROC][{}][{}]'.format(self.name, cmd, procObj.run(cmd)[0]))

                cmd = 'docker cp {}/Asset {}:/AIOPS'.format(self.cmdb_path, container_name_val)
                self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
                self.logger.debug('[{}][SUBPROC][{}][{}]'.format(self.name, cmd, procObj.run(cmd)[0]))

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
