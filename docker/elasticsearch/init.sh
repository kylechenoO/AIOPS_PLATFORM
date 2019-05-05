#!/usr/bin/env bash
docker build . -t aiops_elasticsearch_img
docker run --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v /etc/localtime:/etc/localtime:ro --log-driver=syslog --log-opt tag=elasticsearch --network mynet --ip 1.1.1.6 --dns 223.5.5.5 --dns 223.6.6.6 -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" --hostname elasticsearch --name elasticsearch aiops_elasticsearch_img