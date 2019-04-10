#!/usr/bin/env bash
docker build . -t aiops_db_img
docker run --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro --network mynet -e MYSQL_ROOT_PASSWORD=21478De23a1a1628c944 --ip 1.1.1.5 --dns 223.5.5.5 --dns 223.6.6.6 -d -p 3306:3306 --hostname mariadb --name mariadb aiops_db_img:latest
sleep 10
docker exec -i mariadb mysql -uroot -p21478De23a1a1628c944 < ./db/aiops.ddl
