FROM centos:latest
MAINTAINER Kyle Chen
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
RUN yum clean all && \
    yum makecache && \
    yum upgrade -y && \
    yum install vim openssh-server epel-release -y && \
    yum clean all && \
    yum makecache && \
    yum install python36 python36-devel python36-pip -y && \
    echo "set -o vi" >> /etc/bashrc && \
    pip3.6 install --upgrade pip && \
    pip install ansible && \
    echo "E100c6b506a70553de18" | passwd --stdin root && \
    systemctl enable sshd
