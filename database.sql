CREATE DATABASE pools;
create user pool_editor with encrypted password 'poolEdit12';
grant all privileges on database pools to pool_editor;
#then connect to database using the following command
psql -U pool_editor pools
create table pool(id varchar(255) PRIMARY KEY,name varchar(255));
create table resource(pool_id varchar(255),id varchar(255) PRIMARY KEY,ip_address varchar(255),status varchar(255));
