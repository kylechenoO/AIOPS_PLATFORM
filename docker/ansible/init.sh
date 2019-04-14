#!/usr/bin/env bash
docker build . -t aiops_ansible_img
docker run --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v /etc/localtime:/etc/localtime:ro --network mynet --ip 1.1.1.2 --dns 223.5.5.5 --dns 223.6.6.6 --name ansible --hostname ansible -tdi aiops_ansible_img:latest /usr/sbin/init
