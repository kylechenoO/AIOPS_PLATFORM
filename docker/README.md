# Docker Scripts Dir

- please run `./init.sh` to initial docker network env

# Config hosts with ELK

- run `curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.0.0-x86_64.rpm`
- run `curl -L -O https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-7.0.0-x86_64.rpm`
- run `rpm -ivh install filebeat-7.0.0-x86_64.rpm metricbeat-7.0.0-x86_64.rpm`
- edit `/etc/metricbeat/metricbeat.yml`, change some elasticsearch and kibana config.
- edit `/etc/filebeat/filebeat.yml`, change some elasticsearch and kibana config.
- run `metricbeat modules enable system; metricbeat setup; systemctl enable metricbeat; systemctl start metricbeat`
- run `filebeat modules enable system; filebeat setup; systemctl enable filebeat; systemctl start filebeat`
- open `http://1.1.1.7:5601`, you can find metric and log data.