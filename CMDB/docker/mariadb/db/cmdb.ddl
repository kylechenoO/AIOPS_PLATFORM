
CREATE DATABASE cmdb;
CREATE USER cmdbadm@'1.1.1.0/24' IDENTIFIED BY 'Cbfd63df3fe749e7e631';
GRANT ALL PRIVILEGES ON cmdb.* TO cmdbadm@'1.1.1.0/24';
FLUSH PRIVILEGES;

USE cmdb;

CREATE TABLE cmdb_OS(id VARCHAR(128) PRIMARY KEY,
                id_net_list VARCHAR(10240),
                hardware_id VARCHAR(128),
                hardware_type VARCHAR(16),
                os_type VARCHAR(16),
                os_version VARCHAR(32),
                arch VARCHAR(16),
                kernel VARCHAR(32),
                hostname VARCHAR(32),
                python_version VARCHAR(16),
                installed_pkgs TEXT(102400),
                ip_list VARCHAR(256),
                interface_list VARCHAR(128));

CREATE TABLE cmdb_USER(id VARCHAR(128) PRIMARY KEY,
                    id_os VARCHAR(128),
                    id_group VARCHAR(128),
                    uid INT(8),
                    gid INT(8),
                    user_name VARCHAR(64),
                    home VARCHAR(64),
                    shell VARCHAR(64),
                    status VARCHAR(8));

CREATE TABLE cmdb_GROUP(id VARCHAR(128) PRIMARY KEY,
                    id_os VARCHAR(128),
                    id_user_list VARCHAR(256),
                    gid INT(8),
                    group_name VARCHAR(64),
                    user_list VARCHAR(256));

CREATE TABLE cmdb_PORT(id VARCHAR(128) PRIMARY KEY,
                    id_os VARCHAR(128),
                    id_user VARCHAR(128),
                    id_proc VARCHAR(128),
                    id_neti_list VARCHAR(512),
                    rel_port_list VARCHAR(512),
                    type VARCHAR(16),
                    listening_ip_list VARCHAR(128),
                    port VARCHAR(16),
                    status VARCHAR(16),
                    pid INT(8),
                    neti_list VARCHAR(256),
                    user VARCHAR(16),
                    uid INT(8),
                    dst_ip VARCHAR(16),
                    dst_port VARCHAR(16));

CREATE TABLE cmdb_PROC(id VARCHAR(128) PRIMARY KEY,
                    id_os VARCHAR(128),
                    id_user VARCHAR(128),
                    pid INT(8),
                    proc_name VARCHAR(128),
                    user VARCHAR(16),
                    status VARCHAR(16),
                    command TEXT(102400),
                    environ TEXT(102400));

CREATE TABLE cmdb_NETI(id VARCHAR(128) PRIMARY KEY,
                    id_os VARCHAR(128),
                    interface VARCHAR(32),
                    mac VARCHAR(32),
                    ipv4_ip VARCHAR(32),
                    ipv6_ip VARCHAR(32),
                    ipv4_netmask VARCHAR(32),
                    ipv6_netmask VARCHAR(32),
                    default_nic BOOL,
                    gateway VARCHAR(32),
                    status BOOL);

CREATE TABLE cmdb_DEV(id VARCHAR(128) PRIMARY KEY,
                    id_os VARCHAR(128),
                    id_part_list VARCHAR(512),
                    disk VARCHAR(128),
                    size INT(16),
                    part_list VARCHAR(128));

CREATE TABLE cmdb_PART(id VARCHAR(128) PRIMARY KEY,
                    id_os VARCHAR(128),
                    id_dev VARCHAR(128),
                    disk VARCHAR(128),
                    part VARCHAR(128),
                    type VARCHAR(16),
                    mounted BOOL,
                    mount_point VARCHAR(512),
                    size INT(16),
                    disk_usage VARCHAR(16));

commit;
