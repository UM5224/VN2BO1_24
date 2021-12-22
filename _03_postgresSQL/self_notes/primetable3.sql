create table dept1(  
  deptno     serial primary key,
  dname      varchar(14),  
  loc        varchar(13)  );
 
select * from dept1
drop table dept1

insert into DEPT1 ( DNAME, LOC)
values( 'ACCOUNTING', 'NEW YORK');

insert into dept1 ( DNAME, LOC)  
values( 'RESEARCH', 'DALLAS');

insert into dept1 ( DNAME, LOC)  
values( 'SALES', 'CHICAGO');

insert into dept1  ( DNAME, LOC) 
values( 'OPERATIONS', 'BOSTON');