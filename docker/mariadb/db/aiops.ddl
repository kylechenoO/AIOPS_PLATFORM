CREATE DATABASE aiops;
CREATE USER sqladm@'%' IDENTIFIED BY 'Cbfd63df3fe749e7e631';
GRANT ALL PRIVILEGES ON aiops.* TO sqladm@'%';
FLUSH PRIVILEGES;
USE aiops;

CREATE TABLE cmdb_OS(id VARCHAR(128) PRIMARY KEY,
                id_net_list VARCHAR(10240),
                hardware_id VARCHAR(128),
                hardware_type VARCHAR(128),
                os_type VARCHAR(16),
                os_version VARCHAR(32),
                arch VARCHAR(16),
                kernel VARCHAR(32),
                hostname VARCHAR(32),
                python_version VARCHAR(16),
                installed_pkgs TEXT(102400),
                ip_list VARCHAR(10240),
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
                    id_user_list VARCHAR(1024),
                    gid INT(8),
                    group_name VARCHAR(64),
                    user_list VARCHAR(512));

CREATE TABLE cmdb_PORT(id VARCHAR(128) PRIMARY KEY,
                    id_os VARCHAR(128),
                    id_user VARCHAR(128),
                    id_proc VARCHAR(128),
                    id_neti_list VARCHAR(512),
                    rel_port_list VARCHAR(512),
                    type VARCHAR(16),
                    listening_ip_list VARCHAR(10240),
                    port VARCHAR(16),
                    status VARCHAR(16),
                    pid VARCHAR(16),
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
                    ipv6_ip VARCHAR(128),
                    ipv4_netmask VARCHAR(32),
                    ipv6_netmask VARCHAR(128),
                    default_nic VARCHAR(16),
                    gateway VARCHAR(32),
                    status VARCHAR(8));

CREATE TABLE cmdb_DEV(id VARCHAR(128) PRIMARY KEY,
                    id_os VARCHAR(128),
                    id_part_list VARCHAR(10240),
                    disk VARCHAR(128),
                    size INT(16),
                    part_list VARCHAR(128));

CREATE TABLE cmdb_PART(id VARCHAR(128) PRIMARY KEY,
                    id_os VARCHAR(128),
                    id_dev VARCHAR(128),
                    disk VARCHAR(128),
                    part VARCHAR(128),
                    type VARCHAR(16),
                    mounted VARCHAR(8),
                    mount_point VARCHAR(512),
                    size INT(16),
                    disk_usage VARCHAR(16));

CREATE TABLE cmdb_DOCKER(id VARCHAR(128) PRIMARY KEY,
                    id_os VARCHAR(128),
                    container_id VARCHAR(128),
                    container_name VARCHAR(128),
                    image_name VARCHAR(128),
                    stats VARCHAR(16),
                    status VARCHAR(64),
                    port_dict TEXT(102400),
                    network_setting_dict TEXT(102400),
                    disk_dict TEXT(102400));

CREATE TABLE sys_user(id INT(8) PRIMARY KEY NOT NULL AUTO_INCREMENT,
                    user_name VARCHAR(32) NOT NULL UNIQUE,
                    password VARCHAR(256) NOT NULL,
                    email VARCHAR(64) NOT NULL UNIQUE,
                    group_list VARCHAR(1024),
                    role_list VARCHAR(1024),
                    business_system_list VARCHAR(1024));

CREATE TABLE sys_group(id INT(8) PRIMARY KEY NOT NULL AUTO_INCREMENT,
                    group_name VARCHAR(32) NOT NULL UNIQUE,
                    user_list VARCHAR(1024));

CREATE TABLE sys_role(id INT(8) PRIMARY KEY NOT NULL AUTO_INCREMENT,
                    role_name VARCHAR(32) NOT NULL UNIQUE,
                    is_admin BOOL DEFAULT False,
                    user_list VARCHAR(1024));

CREATE TABLE sys_business_system(id INT(8) PRIMARY KEY NOT NULL AUTO_INCREMENT,
                    system_name VARCHAR(32) NOT NULL UNIQUE,
                    id_os_list VARCHAR(40960));

commit;
