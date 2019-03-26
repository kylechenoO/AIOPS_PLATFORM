#!/usr/bin/env bash
docker run --network mynet --ip 1.1.1.3 --dns 223.5.5.5 --dns 223.6.6.6 -d -p 5672:5672 -p 15672:15672 --hostname rabbitmq1 --name rabbitmq1 rabbitmq:management
docker run --network mynet --ip 1.1.1.4 --dns 223.5.5.5 --dns 223.6.6.6 -d -p 5673:5672 -p 15673:15672 --hostname rabbitmq2 --name rabbitmq2 rabbitmq:management
