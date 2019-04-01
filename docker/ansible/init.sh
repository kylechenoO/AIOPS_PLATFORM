#!/usr/bin/env bash
docker run --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro --network mynet --ip 1.1.1.2 --dns 223.5.5.5 --dns 223.6.6.6 --name ansible --hostname ansible -tdi ansible:latest /usr/sbin/init
