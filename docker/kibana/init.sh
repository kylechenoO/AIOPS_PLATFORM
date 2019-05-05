#!/usr/bin/env bash
docker build . -t aiops_kibana_img
docker run --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v /etc/localtime:/etc/localtime:ro --log-driver=syslog --log-opt tag=kibana --network mynet --ip 1.1.1.7 --dns 223.5.5.5 --dns 223.6.6.6 -d --link elasticsearch:elasticsearch -p 5601:5601 --hostname kibana --name kibana aiops_kibana_img:latest