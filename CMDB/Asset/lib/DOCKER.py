'''
    DOCKER.py Lib
    Written By Kyle Chen
    Version 20190412v1
'''

# import buildin pkgs
import os
import re
import docker
import dmidecode
import datetime
from random import randint

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
        self.title = ['id', 'id_os', 'run_time', 'container_id', 'container_name', 'image_name', 'stats', 'status', 'port_dict', 'network_setting_dict', 'disk_dict']
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
                    self.result = [self.title]
                    return(self.result)

        self.os_id = self.getOSId()
        id_os_val = 'OS-{}'.format(self.os_id)
        self.logger.debug('[{}][id_os][{}]'.format(self.name, id_os_val))
        run_time_val = datetime.datetime.now()
        run_time_val = run_time_val.strftime("%Y-%m-%d %H:%M:%S")
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
            self.result.append([id_val, id_os_val, run_time_val, container_id_val, container_name_val, image_name_val,
                stats_val, status_val, port_dict_val, network_setting_dict_val, disk_dict_val])

            ## push Scheduler, Asset scripts to container
            if stats_val == 'running':
                asset_version = self.getVersion()
                procObj = SubProc(self.logger, self.proc_timeout)
                cmd = 'docker exec -i {} cat /AIOPS/CMDB/Asset/VERSION'.format(container_name_val)
                asset_rversion = procObj.run(cmd)[0].decode('utf-8').strip('\n')
                self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
                self.logger.debug('[{}][SUBPROC][{}][{}]'.format(self.name, cmd, asset_rversion))

                if asset_version != asset_rversion:
                    cmd = 'cat {}/containerCreateDirectory.sh | docker exec -i {} bash'.format(self.scripts_dir, container_name_val)
                    self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
                    self.logger.debug('[{}][SUBPROC][{}][{}]'.format(self.name, cmd, procObj.run(cmd)[0]))

                    cmd = 'docker cp {}/Asset {}:/AIOPS/CMDB'.format(self.cmdb_path, container_name_val)
                    self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
                    self.logger.debug('[{}][SUBPROC][{}][{}]'.format(self.name, cmd, procObj.run(cmd)[0]))

                    cmd = 'docker exec -i {} /opt/Anaconda3/bin/pip install -r /AIOPS/CMDB/Asset/requirements.txt'.format(container_name_val)
                    self.logger.debug('[{}][SUBPROC][{}]'.format(self.name, cmd))
                    self.logger.debug('[{}][SUBPROC][{}][{}]'.format(self.name, cmd, procObj.run(cmd)[0]))

                data = []
                flag_skip = False
                cfg_path = '{}/Scheduler/scheduls/{}'.format(self.cmdb_path, container_name_val)
                if os.path.exists(cfg_path):
                    with open(cfg_path, 'r') as fp:
                        data = fp.read()

                    data = data.split('\n')
                    if data != '':
                        data.remove('')

                    for line in data:
                        if line[0] != '#' and line.find('Asset.py') > -1:
                            flag_skip = True

                if not flag_skip:
                    data.append('{} * * * * docker exec -i {} /opt/Anaconda3/bin/python /AIOPS/CMDB/Asset/bin/Asset.py &> /dev/null &\n'.format(randint(0, 59), container_name_val))
                    with open(cfg_path, 'w') as fp:
                        fp.write('\n'.join(data))

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
        with open('{}/Asset/VERSION'.format(self.cmdb_path)) as fp:
            asset_version = fp.read().strip('\n')

        return(asset_version)
