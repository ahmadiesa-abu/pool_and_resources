CREATE DATABASE pools;
create user pool_editor with encrypted password 'poolEdit12';
grant all privileges on database pools to pool_editor;
#then connect to database using the following command
psql -U pool_editor pools
create table pool(id varchar(255) PRIMARY KEY,name varchar(255));
create table resource(pool_id varchar(255),id varchar(255) PRIMARY KEY,ip_address varchar(255),status varchar(255));

insert into pool values ('fg34sc-re34-12tg-dv34hn12za56','unit_testing_example')
insert into resource values('fg34sc-re34-12tg-dv34hn12za56','i81YoErB-qNUn-OWUi-qIzGavZ9zORt','1.1.1.1','RELEASED');
insert into resource values('fg34sc-re34-12tg-dv34hn12za56','saukR69C-Yr0b-qai5-UL8rTgJMWofR','2.2.2.2','RELEASED');
insert into resource values('fg34sc-re34-12tg-dv34hn12za56','ds8X8PZY-qf4B-UfTg-CcuTx0YkVa2U','3.3.3.3','ALLOCATED');
commit;
