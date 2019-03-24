# CMDB Backend

## The data structure of CMDB data collector

### Data Structor

![](../pic/cmdb_ds.png)

### CI Types

#### Update by scripts

|CI Type|Comment|ID|Related|
|:-:|:-:|:-:|:-:|
|OS|OS Info|id|NETI_ID|
|USER|USER Info|id|OS_ID|
|GROUP|GROUP Info|id|OS_ID, USER_ID|
|PORT|PORT Info|id|OS_ID, NETI_ID|
|PROC|PROCESS Info|id|OS_ID, PORT_ID, USER_ID|
|NETI|NET Interface Info|id|OS_ID|
|DEV|DEVICE Info|id|OS_ID|
|PART|PARTITION Info|id|OS_ID, DEV_ID|

#### Update by people

|CI Type|Comment|ID|Related|
|:-:|:-:|:-:|:-:|
|SYSUSER|SYSUSER Info|id|SYSUSER_ID|
|BSYS|BSYS Info|id|BSYS_ID|
|SUBSYS|SUBSYS Info|id|OS_ID, BSYS_ID|

### OS TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id|cat /sys/devices/virtual/dmi/id/product_uuid \| sed -e 's/-//g' -e 's/^/OS-/'|OS-a170790ce6a6fc782db058324a912dac|OS_ID|||
|id_neti_list|NETI-${OS_ID}-interface, NETI-${OS_ID}-interface|NETI-a170790ce6a6fc782db058324a912dac-en9, NETI-a170790ce6a6fc782db058324a912dac-en10|Related to NETI|NETI_ID|
|hardware_id|cat /sys/devices/virtual/dmi/id/product_uuid|a170790ce6a6fc782db058324a912dac||||
|hardware_type|dmidecode -s system-product-name|Hardware\|Docker\|VMWare|if is hardware or vmware, can get from command, if not can get from the docker server by docker ps -a(There's a CONTAINER_ID here)||
|os_type|lsb_release -a|Linux\|Windows|run command||
|os_version|cat /proc/version|Ubuntu\|CentOS|read the file or fetch it from ansible||
|arch|uname -a|i386\|x86_64|run command||
|kernel|uname -r|4.12.0-42-generic|read the file or fetch it from ansible||
|hostname|hostname|node1|run command||
|python_version|python -V|Python 3.6.0|run command||
|installed_pkgs|rpm -qa\|dpkg -l|a long list|run command||
|ip_list|ifconfig -a\|ip addr list|1.1.1.1|run command||
|interface_list|ifconfig -a\|ip addr list|en9|run command||

### USER TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id|USER-${OS_ID}-uid|USER-a170790ce6a6fc782db058324a912dac-0|USER_ID|OS_ID|
|id_os|OS-${OS_ID}|OS-a170790ce6a6fc782db058324a912dac|Related to OS_ID|OS_ID|
|id_group|cat /etc/passwd|GROUP-a170790ce6a6fc782db058324a912dac-0|Related to GROUP_ID|GROUP_ID|
|uid|cat /etc/passwd|0|read file||
|gid|cat /etc/passwd|0|read file||
|user_name|cat /etc/passwd|root|read file||
|home|cat /etc/passwd|/root|read file||
|shell|cat /etc/passwd|/bin/bash|read file||
|status|cat /etc/shadow|True|read file||

### GROUP TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id|GROUP-${OS_ID}-gid|GROUP-a170790ce6a6fc782db058324a912dac-0|GROUP_ID|OS_ID|
|id_os|OS-${OS_ID}|OS-a170790ce6a6fc782db058324a912dac|Related to OS_ID|OS_ID|
|id_user_list|USER-${OS_ID}-uid|USER-a170790ce6a6fc782db058324a912dac-0,USER-a170790ce6a6fc782db058324a912dac-1|Related to USER_ID|USER_ID|
|gid|cat /etc/group|0|read file||
|group_name|cat /etc/group|root|read file||
|user_list|cat /etc/group|root|read file||

### PORT TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id|PORT-${OS_ID}-TCP\|UDP-port|PORT-a170790ce6a6fc782db058324a912dac-TCP-22|PORT_ID|OS_ID|
|id_os|OS-${OS_ID}|OS-a170790ce6a6fc782db058324a912dac|Related to OS_ID|OS_ID|
|id_user|USER-${OS_ID}-uid|USER-a170790ce6a6fc782db058324a912dac-0|Related to USER_ID|USER_ID|
|id_proc_list|PROC-${OS_ID}-pid|PROC-a170790ce6a6fc782db058324a912dac-4679|Related to PROC_ID|PROC_ID|
|id_neti_list|NETI-${OS_ID}-interface|NETI-${OS_ID}-en9, NETI-${OS_ID}-en10|each item is related to a NETI_ID|NETI_ID|
|rel_port_list|REL-PORT-LISTENING-${LISTENING_IP}-${TYPE}-${PORT}\|REL-PORT-CLIENT-${SERVER_IP}-${TYPE}-${SERVER_PORT}|REL-PORT-LISTENING-1.1.1.1-TCP-22\|REL-PORT-CLIENT-1.1.1.1-TCP-22|PORT RELATIONS|rel_port|
|type|lsof -i -n -P\|netstat -luntp|TCP\|UDP|run command, different command between hardware os and docker||
|port|lsof -i -n -P\|netstat -luntp|22|run command, different command between hardware os and docker||
|status|lsof -i -n -P\|netstat -luntp|LISTENING\|ESTABLISHED|run command, different command between hardware os and docker||
|pid_list|lsof -i -n -P|4679|run command, still not find a best way to docker host||
|listening_ip_list|lsof -i -n -P\|netstat -luntp|1.1.1.1, 2.2.2.2|need to match with $(ifconfig -a \| ip addr list)||
|neti_list|ifconfig -a \| ip addr list|en9, en10|run command||
|user|lsof -i -n -P|root|run command, still not find a best way to docker host||
|uid|cat /etc/passwd|0|read file||
|dst_ip|lsof -i -n -P|1.1.1.2|if the state is ESTABLISHED need to get this data, a connection to another server(can query from the NETI)||
|dst_port|lsof -i -n -P|3306|if the state is ESTABLISHED need to get this data, a connection to another server||

### PROC TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id|PROC-${OS_ID}-pid|PROC-a170790ce6a6fc782db058324a912dac-4679|PROC_ID|OS_ID|
|id_os|OS-${OS_ID}|OS-a170790ce6a6fc782db058324a912dac|Related to OS_ID|OS_ID|
|id_user|USER-${OS_ID}-uid|USER-a170790ce6a6fc782db058324a912dac-0|USER_ID|USER_ID|
|pid|ps -elf|4679|run command||
|proc_name|ps -elf|sshd|run command||
|user_name|ps -elf|root|run command||
|status|ps -elf|S|run command||
|command|ps -elf|/usr/sbin/sshd -D|run command||
|environ|ps ewww -p ${pid}|/usr/sbin/sshd -D LANG=en_US.UTF-8 PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin NOTIFY_SOCKET=/run/systemd/notify INVOCATION_ID=32fc790ce6a6fc782dcw48324a912dwb JOURNAL_STREAM=2:3293 SSHD_OPTS=|run command||

### NETINTERFACE TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id|NETI-${OS_ID}-interface|NET-${OS_ID}-en9|NETI_ID||
|id_os|OS-${OS_ID}|OS-a170790ce6a6fc782db058324a912dac|Related to OS_ID|OS_ID|
|interface|ifconfig -a \| ip addr list|en9|run command||
|mac|ifconfig -a \| ip addr list|00:00:00:00:00:00|run command||
|ipv4_ip|ifconfig -a \| ip addr list|1.1.1.1|run command||
|ipv6_ip|ifconfig -a \| ip addr list|1.1.1.1|run command||
|ipv4_netmask|ifconfig -a \| ip addr list|1.1.1.1|run command||
|ipv6_netmask|ifconfig -a \| ip addr list|1.1.1.1|run command||
|default_nic|ifconfig -a \| ip addr list|1.1.1.1|run command||
|gateway|ifconfig -a \| ip addr list|1.1.1.1|run command||
|status|ifconfig -a \| ip addr list|UP\|DOWN|run command||

### DEV TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id|DEV-${OS_ID}-disk|DEV-${OS_ID}-sdd|DEV_ID|OS_ID|
|id_os|OS-${OS_ID}|OS-a170790ce6a6fc782db058324a912dac|Related to OS_ID|OS_ID|
|id_part_list|PART-${OS_ID}-part|PART-a170790ce6a6fc782db058324a912dac-sdd1, PART-a170790ce6a6fc782db058324a912dac-sdd2|Related to each PART_ID|PART_ID|
|disk|fdisk -l|sdd|run command||
|size|fdisk -l|sdd|run command||
|part_list|fdisk -l|sdd1, sdd2|run command||

### PART TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id|PART-${OS_ID}-part|PART-${OS_ID}-sdd1|PART_ID|OS_ID|
|id_os|OS-${OS_ID}|OS-a170790ce6a6fc782db058324a912dac|Related to OS_ID|OS_ID|
|id_dev|DEV-${OS_ID}-disk|DEV-${OS_ID}-sdd|DEV_ID|OS_ID|
|disk|fdisk -l|sdd|run command||
|part|fdisk -l|sdd1|run command||
|mounted|mount|True\|False|run command||
|mount_point|mount|/tmp/ttt|run command||
|size|df -h|10G|run command||
|usage|df -h|10%|run command||

### SYSUSER TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id||00000001|SYSUSER_ID||
|id_bsys_list||00000001, 00000002|||
|user_name||admin|||
|password||xxxxxx|||

### BSYS TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id||00000001|BSYS_ID||
|id_subbsys_list||nginx, tomcat|||
|name||admin|||

### SUBBSYS TYPE

|Item|Command|Sample|Comment|Related|
|:-:|:-:|:-:|:-:|:-:|
|id||00000001|SUBSYS_ID||
|id_os_list||OS-a170790ce6a6fc782db058324a912dac, OS-a170790ce6a6fc782db058324a912232|||
|name||admin|||

## Ansible

- I just write a Dockerfile and boot script in `ansible/`. You can read the README.md file, and boot it.
- In the next steps, I will use ansible to deploy and run some scripts, to get data, and push them to a Queue.

## RabbitMQ

- I use RabbitMQ to receive and ETL to fetch data.

## ETL

- I use ETL to extract data from RabbitMQ, transform them into database struct, and insert them into database.