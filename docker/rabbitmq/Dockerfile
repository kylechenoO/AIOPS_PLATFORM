FROM rabbitmq:management
MAINTAINER Kyle Chen
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt upgrade -y && \
    apt install wget dmidecode gcc -y && \
    wget -c http://hacking-linux.oss-cn-hongkong.aliyuncs.com/tools/Anaconda3-2019.03-Linux-x86_64.sh -O /opt/Anaconda3-2019.03-Linux-x86_64.sh && \
    bash /opt/Anaconda3-2019.03-Linux-x86_64.sh -b -p /opt/Anaconda3 && \
    echo "set -o vi" >> /etc/profile && \
    echo "export LD_LIBRARY_PATH=/opt/Anaconda3/lib/:$LD_LIBRARY_PATH" >> /etc/profile && \
    echo "export PATH=/opt/Anaconda3/bin/:$PATH" >> /etc/profile
