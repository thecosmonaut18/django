show databases;
create database day1;
use day1;

-- create table student1(rollno int not null,
-- name varchar(30) not null,
-- ph int);

-- insert into student1(rollno,name,ph)value(101,'anu',3456789012);
-- insert into student1 (rollno,ph)value(102,9876543210);
-- insert into student1 (name,ph)value('ais',9995791282);

-- select * from student1


-- create table student2(rollno int not null,
-- name varchar(30) not null,
-- age int check (age>18));

-- insert into student2(rollno,name,age)value(101,'anu',20);
-- insert into student2(rollno,name,age)value(102,"ammu",17);
-- insert into student2(rollno,name,age)value(103,'ais',12);

-- select * from student2


-- create table student3(rollno int not null,
-- name varchar(30) not null,
-- age int default 18);

-- insert into student3(rollno,name,age)value(101,'anu',20);
-- insert into student3(rollno,name,age)value(102,"ammu",17);
-- insert into student3(rollno,name)value(103,'ais');

-- select * from student3

-- create table student4(rollno int not null,
-- name varchar(30) not null,
-- email varchar(30) default "mail",
-- age int default 18,
-- primary key(rollno));

-- create table mark(markid int not null,
-- roll_no int,
-- mark1 int,
-- mark2 int,
-- primary key(markid),
-- foreign key(roll_no)references student4(rollno));

-- insert into student4(rollno,name,age)
-- values(1001,'Ammu',23),
-- (1002,'Jilson',22),
-- (1003,'Ais',22),
-- (1004,'Swathi',22);

-- insert into mark(markid,roll_no,mark1,mark2)
-- values(101,1001,86,89),
-- (102,1003,100,100),
-- (103,1004,95,85),
-- (104,1002,99,99);

-- -- select * from student4 

-- select * from mark


create table student5(slno int,name varchar(20),place varchar(20),course varchar(10),total_mark int);
insert into student5 values(101,'Ammu','Kollam','CS',92),
(102,'Kiran','Thr','EC',24),
(104,'Rani','Kochi','CS',56),
(105,'Raj','Kollam','IT',70);
insert into student5(slno,name)value(106,'Ram');

select * from student5;
#####like

select name from student5 where name like 'a%';
select name from student5 where name like '%n';
select name from student5 where name like '_a%';
select name from student5 where name like '%a%';
select name from student5 where name like '%a_';

#####COUNT

select count(*) from student5 ;
select count(*) as tot from student5 ;
select count(slno) from student5;
select count(course) from student5 where course='CS';

#####MIN MAX

select min(slno) from student5;
select max(slno) from student5;

#####SUM

select sum(slno) from student5;

#####AVERAGE

select avg(slno) from student5;

#####ORDER BY

select * from student5 order by total_mark;

select * from student5 order by total_mark desc;

#####GROUP BY

select course,count(course)from student5 group by course;
