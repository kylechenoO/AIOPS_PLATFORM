# Scheduler Scripts
- This dir is supposed to save some scheduler scripts, it was called by the system crontabl process, and decide when we run wich part.
- Put all the schedul tasks into 'scheduls/' dir.
- All things runs well in Python3.6.

## Setup running env
- run `pip install -r ./requirements.txt`

## Add Scheduler to crontab
- run `crontab -e`, and add this line `* * * * * python3.6 /AIOPS/CMDB/Scheduler/bin/Scheduler.py &> /dev/null &`.
