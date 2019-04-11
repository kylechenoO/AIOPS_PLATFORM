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
                    self.result = [self.title, [''] * len(self.title)]
                    return(self.result)

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
            port_dict_val = re.sub("'", '', str(line['Ports']))
            network_setting_dict_val = re.sub("'", '', str(line['NetworkSettings']))
            disk_dict_val = re.sub("'", '', str(line['Mounts']))
            self.result.append([id_val, id_os_val, container_id_val, container_name_val, image_name_val,
                stats_val, status_val, port_dict_val, network_setting_dict_val, disk_dict_val])

            ## push Scheduler, Asset scripts to container
            if stats_val == 'running':
                asset_version, scheduler_version = self.getVersion()
                procObj = SubProc(self.logger, self.proc_timeout)
                cmd = 'docker exec -i {} cat /AIOPS/CMDB/Asset/VERSION'.format(container_name_val)
                asset_rversion = procObj.run(cmd)[0].decode('utf-8').strip('\n')
                self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
                self.logger.debug('[{}][SUBPROC][{}][{}]'.format(self.name, cmd, asset_rversion))

                cmd = 'docker exec -i {} cat /AIOPS/CMDB/Scheduler/VERSION'.format(container_name_val)
                scheduler_rversion = procObj.run(cmd)[0].decode('utf-8').strip('\n')
                self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
                self.logger.debug('[{}][SUBPROC][{}][{}]'.format(self.name, cmd, scheduler_rversion))

                if scheduler_version != scheduler_rversion:
                    cmd = 'cat {}/containerCreateDirectory.sh | docker exec -i {} bash'.format(self.scripts_dir, container_name_val)
                    self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
                    self.logger.debug('[{}][SUBPROC][{}][{}]'.format(self.name, cmd, procObj.run(cmd)[0]))

                    cmd = 'docker cp {}/Scheduler {}:/AIOPS/CMDB'.format(self.cmdb_path, container_name_val)
                    self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
                    self.logger.debug('[{}][SUBPROC][{}][{}]'.format(self.name, cmd, procObj.run(cmd)[0]))

                    cmd = 'docker exec -i {} /opt/Anaconda3/bin/python /AIOPS/CMDB/Scheduler/scripts/getRandMin.py'.format(container_name_val)
                    self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
                    self.logger.debug('[{}][SUBPROC][{}][{}]'.format(self.name, cmd, procObj.run(cmd)[0]))

                    cmd = 'docker exec -i {} /opt/Anaconda3/bin/pip install -r /AIOPS/CMDB/Scheduler/requirements.txt'.format(container_name_val)
                    self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
                    self.logger.debug('[{}][SUBPROC][{}][{}]'.format(self.name, cmd, procObj.run(cmd)[0]))

                if asset_version != asset_rversion:
                    cmd = 'docker cp {}/Asset {}:/AIOPS/CMDB'.format(self.cmdb_path, container_name_val)
                    self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
                    self.logger.debug('[{}][SUBPROC][{}][{}]'.format(self.name, cmd, procObj.run(cmd)[0]))

                    cmd = 'docker exec -i {} /opt/Anaconda3/bin/pip install -r /AIOPS/CMDB/Asset/requirements.txt'.format(container_name_val)
                    self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
                    self.logger.debug('[{}][SUBPROC][{}][{}]'.format(self.name, cmd, procObj.run(cmd)[0]))

                ## check and add crontab
                cmd = 'docker exec -i {} /opt/Anaconda3/bin/python /AIOPS/CMDB/Scheduler/scripts/addCrontab.py'.format(container_name_val)
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

    ## get Asset, Scheduler VERSION
    def getVersion(self):
        asset_version = ''
        scheduler_version = ''
        with open('{}/Asset/VERSION'.format(self.cmdb_path)) as fp:
            asset_version = fp.read().strip('\n')

        with open('{}/Scheduler/VERSION'.format(self.cmdb_path)) as fp:
            scheduler_version = fp.read().strip('\n')

        return(asset_version, scheduler_version)
