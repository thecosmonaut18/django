show databases;
create database shop;
use shop;

create table salesman(salesman_id int,
name varchar(30),
city varchar(30),
commission float(30));

insert into salesman (salesman_id,name,city,commission)value(5001,'James Hoog','New York',0.15);
insert into salesman (salesman_id,name,city,commission)value(5002,'Nail Knite','Paris',0.13);
insert into salesman (salesman_id,name,city,commission)value(5005,'Pit Alex','London',0.11);
insert into salesman (salesman_id,name,city,commission)value(5006,'Mc Lyon','Paris',0.14);
insert into salesman (salesman_id,name,city,commission)value(5003,'Lauson Hen','',0.12);
insert into salesman (salesman_id,name,city,commission)value(5007,'Paul Adam','Rome',0.13);


select * from salesman;