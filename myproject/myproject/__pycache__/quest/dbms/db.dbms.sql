create database day3;
use day3;

insert into employee values(1001,'jilson',1001),(1002,'anu',1001),(1003,'gopi',1002),(1004,'ammu',1002),(1005,'ais',1003);


select * from employee;

select e.name as Employee,m.name as Manager from employee e join employee m on e.mid=m.idemp;

