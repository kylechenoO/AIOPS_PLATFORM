#!/usr/bin/env bash
docker build . -t aiops_rabbitmq_img
## docker run --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro --network mynet --ip 1.1.1.4 --dns 223.5.5.5 --dns 223.6.6.6 -d -p 5673:5672 -p 15673:15672 --hostname rabbitmq2 --name rabbitmq2 aiops_rabbitmq_img:latest
docker run --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro --network mynet --ip 1.1.1.3 --dns 223.5.5.5 --dns 223.6.6.6 -d -p 5672:5672 -p 15672:15672 --hostname rabbitmq --name rabbitmq aiops_rabbitmq_img:latest
