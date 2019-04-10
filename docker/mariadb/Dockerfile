FROM mariadb:latest
MAINTAINER Kyle Chen
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    http_proxy='http://192.168.1.254:1081/' apt upgrade -y && \
    http_proxy='http://192.168.1.254:1081/' apt install wget dmidecode gcc openssh-server openssh-client -y && \
    wget -c http://hacking-linux.oss-cn-hongkong.aliyuncs.com/tools/Anaconda3-2019.03-Linux-x86_64.sh -O /opt/Anaconda3-2019.03-Linux-x86_64.sh && \
    bash /opt/Anaconda3-2019.03-Linux-x86_64.sh -b -p /opt/Anaconda3 && \
    echo "set -o vi" >> /etc/profile && \
    echo "export LD_LIBRARY_PATH=/opt/Anaconda3/lib/:$LD_LIBRARY_PATH" >> /etc/profile && \
    echo "export PATH=/opt/Anaconda3/bin/:$PATH" >> /etc/profile && \
    echo "root:917F1E188f7097c286ad" | chpasswd && \
    systemctl enable ssh
