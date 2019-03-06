# CMDB Backend

## The data structure of CMDB data collector

### CI Types

|CI Type|Comment|ID|Related|
|:-:|:-:|:-:|:-:|
|OS|OS Info|id||
|USER|USER Info|id|OS_ID|
|GROUP|GROUP Info|id|OS_ID, USER_ID|
|PORT|PORT Info|id|OS_ID, NETI_ID|
|PROC|PROCESS Info|id|OS_ID, PORT_ID, USER_ID|
|NETI|NET Interface Info|id|OS_ID|
|DEV|DEVICE Info|id|OS_ID|

### OS TYPE

- Hardware OS

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id|cat /sys/devices/virtual/dmi/id/product_uuid \| sed -e 's/-//g' -e 's/^/OS-/'|OS-a170790ce6a6fc782db058324a912dac|OS_ID|||
|hardware_id|cat /sys/devices/virtual/dmi/id/product_uuid|a170790ce6a6fc782db058324a912dac||||
|hardware_type|dmidecode -s system-product-name|Hardware\|Docker\|VMWare|if is hardware or vmware, can get from command, if not can get from the docker server by docker ps -a(There's a CONTAINER_ID here)||
|os_type|cat /proc/version|Ubuntu\|CentOS|read the file or fetch it from ansible||
|kernel|uname -r|4.12.0-42-generic|read the file or fetch it from ansible||
|python_version|python -V|Python 3.6.0|run command||
|installed_pkgs|rpm -qa\|dpkg -l|a long list|run command||

### USER TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id|USER-${OS_ID}-uid|USER-a170790ce6a6fc782db058324a912dac-0|USER_ID|OS_ID|
|uid|cat /etc/passwd|0|read file||
|gid|cat /etc/passwd|0|read file||
|userName|cat /etc/passwd|root|read file||
|home|cat /etc/passwd|/root|read file||
|shell|cat /etc/passwd|/bin/bash|read file||
|status|cat /etc/shadow|True|read file||
|idGroup|cat /etc/passwd|GROUP-a170790ce6a6fc782db058324a912dac-0|read file|GROUP_ID|

### GROUP TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id|GROUP-${OS_ID}-gid|GROUP-a170790ce6a6fc782db058324a912dac-0|GROUP_ID|OS_ID|
|gid|cat /etc/group|0|read file||
|groupName|cat /etc/group|root|read file||
|users|cat /etc/group|root|read file||

### PORT TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id|PORT-TCP\|UDP-${OS_ID}-port|PORT-TCP-a170790ce6a6fc782db058324a912dac-22|PORT_ID|OS_ID|
|type|lsof -i -n -P\|netstat -luntp|TCP\|UDP|run command, different command between hardware os and docker||
|port|lsof -i -n -P\|netstat -luntp|22|run command, different command between hardware os and docker||
|state|lsof -i -n -P\|netstat -luntp|LISTENING\|ESTABLISHED|run command, different command between hardware os and docker||
|pid|lsof -i -n -P|4679|run command, still not find a best way to docker host||
|listeningIPs|lsof -i -n -P\|netstat -luntp|1.1.1.1, 2.2.2.2|need to match with $(ifconfig -a \| ip addr list)||
|netis|ifconfig -a \| ip addr list|en9, en10|run command||
|user|lsof -i -n -P|root|run command, still not find a best way to docker host||
|uid|cat /etc/passwd|0|read file||
|idUser|USER-${OS_ID}-uid|USER-a170790ce6a6fc782db058324a912dac-0|related to USER_ID|USER_ID|
|idProc|PROC-${OS_ID}-pid|PROC-a170790ce6a6fc782db058324a912dac-4679|related to PROC_ID|PROC_ID|
|idNeti|NETI-${OS_ID}-interface|NET-${OS_ID}-en9, NET-${OS_ID}-en10|each item is related to a NETI_ID|NETI_ID|

### PROC TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id|PROC-${OS_ID}-pid|PROC-a170790ce6a6fc782db058324a912dac-4679|PROC_ID|OS_ID|
|pid|ps -elf|4679|run command||
|procName|ps -elf|sshd|run command||
|user|ps -elf|root|run command||
|state|ps -elf|S|run command||
|command|ps -elf|/usr/sbin/sshd -D|run command||
|longCommand|ps ewww -p ${pid}|/usr/sbin/sshd -D LANG=en_US.UTF-8 PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin NOTIFY_SOCKET=/run/systemd/notify INVOCATION_ID=32fc790ce6a6fc782dcw48324a912dwb JOURNAL_STREAM=2:3293 SSHD_OPTS=|run command||
|idUser|USER-${OS_ID}-uid|USER-a170790ce6a6fc782db058324a912dac-0|USER_ID|USER_ID|

### NETINTERFACE TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id|NETI-${OS_ID}-interface|NET-${OS_ID}-en9|NETI_ID|OS_ID|
|interface|ifconfig -a \| ip addr list|en9|run command||
|mac|ifconfig -a \| ip addr list|00:00:00:00:00:00|run command||
|ip|ifconfig -a \| ip addr list|1.1.1.1|run command||
|netmask|ifconfig -a \| ip addr list|255.255.255.0|run command||
|status|ifconfig -a \| ip addr list|UP\|DOWN|run command||
|broadcast|ifconfig -a \| ip addr list|1.1.1.255|run command||

### DEVICE TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id|DEV-${OS_ID}-disk|DEV-${OS_ID}-sdd|DEV_ID|OS_ID|
|disk|fdisk -l|sdd|run command||
|partitions|fdisk -l|sdd1|run command||
|mounted|mount|True\|False|run command||
|mountPoint|mount|/tmp/ttt|run command||


