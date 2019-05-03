FROM centos:latest
MAINTAINER Kyle Chen
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
RUN yum clean all && \
    yum makecache && \
    yum upgrade -y && \
    yum install vim openssh-server epel-release gcc glibc wget bzip2 dmidecode -y && \
    wget -c http://hacking-linux.oss-cn-hongkong.aliyuncs.com/tools/Anaconda3-2019.03-Linux-x86_64.sh -O /opt/Anaconda3-2019.03-Linux-x86_64.sh && \
    bash /opt/Anaconda3-2019.03-Linux-x86_64.sh -b -p /opt/Anaconda3 && \
    echo "set -o vi" >> /root/.bashrc && \
    echo "export LD_LIBRARY_PATH=/opt/Anaconda3/lib/:$LD_LIBRARY_PATH" >> /root/.bashrc && \
    echo "export PATH=/opt/Anaconda3/bin/:$PATH" >> /root/.bashrc && \
    /opt/Anaconda3/bin/pip install ansible && \
    echo "E100c6b506a70553de18" | passwd --stdin root && \
    systemctl enable sshd
