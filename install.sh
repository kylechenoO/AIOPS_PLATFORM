#!/usr/bin/env bash
if [ $(pwd) != "/AIOPS" ]
then

    echo "Please put this directory in '/', and rename it as '/AIOPS'."
    exit -1

fi

if [ -f /etc/redhat-release ]
then
    yum clean all
    yum makecache
    yum upgrade -y
    yum install vim openssh-server epel-release gcc glibc wget bzip2 dmidecode -y
    wget -c http://hacking-linux.oss-cn-hongkong.aliyuncs.com/tools/Anaconda3-2019.03-Linux-x86_64.sh -O /opt/Anaconda3-2019.03-Linux-x86_64.sh
    bash /opt/Anaconda3-2019.03-Linux-x86_64.sh -b -p /opt/Anaconda3
    echo "set -o vi" >> /root/.bashrc
    echo "export LD_LIBRARY_PATH=/opt/Anaconda3/lib/:$LD_LIBRARY_PATH" >> /root/.bashrc
    echo "export PATH=/opt/Anaconda3/bin/:$PATH" >> /root/.bashrc
    /opt/Anaconda3/bin/pip install -r /AIOPS/Scheduler/requirements.txt
    /opt/Anaconda3/bin/pip install -r /AIOPS/CMDB/Asset/requirements.txt
    /opt/Anaconda3/bin/pip install -r /AIOPS/CMDB/ETL/requirements.txt
    /opt/Anaconda3/bin/pip install -r /AIOPS/WebApp/requirements.txt
    FLAG=$(crontab -l | awk 'BEGIN{ result = "False"; }/^#/{ next; }{ if($0 == "* * * * * /opt/Anaconda3/bin/python /AIOPS/Scheduler/bin/Scheduler.py &> /dev/null &"){ result = "True"; } }END{ printf("%s", result); }')
    if [ ${FLAG} == False ]
    then
        crontab -l > conf
        echo '* * * * * /opt/Anaconda3/bin/python /AIOPS/Scheduler/bin/Scheduler.py &> /dev/null &' >> conf
        crontab conf
        /opt/Anaconda3/bin/python /AIOPS/Scheduler/bin/Scheduler.py

    fi

else
    apt update
    apt upgrade -y
    apt install wget dmidecode gcc -y
    wget -c http://hacking-linux.oss-cn-hongkong.aliyuncs.com/tools/Anaconda3-2019.03-Linux-x86_64.sh -O /opt/Anaconda3-2019.03-Linux-x86_64.sh
    bash /opt/Anaconda3-2019.03-Linux-x86_64.sh -b -p /opt/Anaconda3
    echo "set -o vi" >> /root/.bashrc
    echo "export LD_LIBRARY_PATH=/opt/Anaconda3/lib/:$LD_LIBRARY_PATH" >> /root/.bashrc
    echo "export PATH=/opt/Anaconda3/bin/:$PATH" >> /root/.bashrc
    /opt/Anaconda3/bin/pip install -r /AIOPS/Scheduler/requirements.txt
    /opt/Anaconda3/bin/pip install -r /AIOPS/CMDB/Asset/requirements.txt
    /opt/Anaconda3/bin/pip install -r /AIOPS/CMDB/ETL/requirements.txt
    /opt/Anaconda3/bin/pip install -r /AIOPS/WebApp/requirements.txt
    FLAG=$(crontab -l | awk 'BEGIN{ result = "False"; }/^#/{ next; }{ if($0 == "* * * * * /opt/Anaconda3/bin/python /AIOPS/Scheduler/bin/Scheduler.py &> /dev/null &"){ result = "True"; } }END{ printf("%s", result); }')
    if [ ${FLAG} == False ]
    then
        crontab -l > conf
        echo '* * * * * /opt/Anaconda3/bin/python /AIOPS/Scheduler/bin/Scheduler.py &> /dev/null &' >> conf
        crontab conf
        /opt/Anaconda3/bin/python /AIOPS/Scheduler/bin/Scheduler.py

    fi

fi
