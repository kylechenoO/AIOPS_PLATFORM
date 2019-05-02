#!/usr/bin/env bash
docker build . -t aiops_mariadb_img
docker run --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v /etc/localtime:/etc/localtime:ro --network mynet -e MYSQL_ROOT_PASSWORD=21478De23a1a1628c944 --ip 1.1.1.5 --dns 223.5.5.5 --dns 223.6.6.6 -d -p 3306:3306 --hostname mariadb --name mariadb aiops_mariadb_img:latest
sleep 10
docker exec -i mariadb mysql -uroot -p21478De23a1a1628c944 < ./db/aiops.ddl
docker exec -i mariadb apt install curl rsyslog -y
docker exec -i mariadb service rsyslog start
docker exec -i mariadb curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.0.0-amd64.deb
docker exec -i mariadb dpkg -i filebeat-7.0.0-amd64.deb
docker cp src/filebeat.yml mariadb:/etc/filebeat/filebeat.yml
docker exec -i mariadb filebeat modules enable system
docker exec -i mariadb filebeat setup
docker exec -i mariadb service filebeat start
docker exec -i mariadb curl -L -O https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-7.0.0-amd64.deb
docker exec -i mariadb dpkg -i metricbeat-7.0.0-amd64.deb
docker cp src/metricbeat.yml mariadb:/etc/metricbeat/metricbeat.yml
docker exec -i mariadb metricbeat modules enable system
docker exec -i mariadb metricbeat setup
docker exec -i mariadb service metricbeat start
