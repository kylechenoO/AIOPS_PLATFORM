import os
import sys

cfg_path = ''
if os.path.exists('/var/spool/cron/crontabs'):
    cfg_path = '/var/spool/cron/crontabs/root'

else:
    cfg_path = '/var/spool/cron/root'

with open(cfg_path, 'r') as fp:
    data = fp.read()

data = data.split('\n')
if data != '':
    data.remove('')

for line in data:
    if line[0] != '#' and line.find('Scheduler.py') > -1:
        sys.exit(0)

data.append('* * * * * /opt/Anaconda3/bin/python /AIOPS/CMDB/Scheduler/bin/Scheduler.py &> /dev/null &\n')
with open(cfg_path, 'w') as fp:
    fp.write('\n'.join(data))
