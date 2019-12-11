FROM rabbitmq:management
MAINTAINER Kyle Chen
USER root
ENV LANG C.UTF-8
COPY src/etc/pip.conf /etc/pip.conf
RUN apt update && \
    apt upgrade -y && \
    apt install wget dmidecode gcc -y && \
    wget -c http://hacking-linux.oss-cn-hongkong.aliyuncs.com/tools/Anaconda3-2019.03-Linux-x86_64.sh -O /opt/Anaconda3-2019.03-Linux-x86_64.sh && \
    bash /opt/Anaconda3-2019.03-Linux-x86_64.sh -b -p /opt/Anaconda3 && \
    echo "set -o vi" >> /root/.bashrc && \
    echo "export LD_LIBRARY_PATH=/opt/Anaconda3/lib/:$LD_LIBRARY_PATH" >> /root/.bashrc && \
    echo "export PATH=/opt/Anaconda3/bin/:$PATH" >> /root/.bashrc
