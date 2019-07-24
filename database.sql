CREATE DATABASE pools;
create table pool(id varchar(255) PRIMARY KEY,name varchar(255));
create table resource(pool_id varchar(255),id varchar(255) PRIMARY KEY,ip_address varchar(255),status varchar(255));