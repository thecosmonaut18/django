show databases;
create database jilson;
use jilson;


create table student(rollno int,
name varchar(30),
email varchar(30),
ph bigint);

alter table student rename to studentdetails;
alter table studentdetails drop email;
alter table student add place varchar(40);


insert into student (rollno,name,ph,place)value(101,'anu',3456789012,'ekm');
insert into student (rollno,name,ph,place)value(102,'jil',9876543210,'kochi');
insert into student (rollno,name,ph,place)value(103,'ais',9995791282,'plrthy');

insert into student(rollno,name,email,ph,place)
values(104,'cos','cosmail',987,'ekm');

insert into student(rollno,name,email,ph,place)
values(104,'cos','cosmail',987,'ekm');

-- delete from student WHERE rollno=101;

-- delete from student where rollno=104;

-- select * from student where name='jil' or rollno=103

update student set name='josna',ph=9074404809 where rollno=104;
select * from student;

update student set email='mailmail';

 