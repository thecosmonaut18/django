show databases;
create database day2;
use day2;

create table student1(rollno int not null,
name varchar(30) not null,
ph int);

insert into student1(rollno,name,ph)value(101,'anu',3456789012);
insert into student1 (rollno,name,ph)value(102,9876543210);
insert into student1 (rollno,name,ph)value('ais',9995791282);

select * from student1