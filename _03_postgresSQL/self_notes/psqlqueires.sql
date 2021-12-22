create table country(
cname varchar(50),
clanguage varchar(50),
cid int);


insert into country values('india','hindi',10);

insert into country values('china','chinese',20);

insert into country values('england','english',30);

select * from persons;
select * from country;

create table persons(
pname varchar(50),
pnumber int);
drop table persons;

insert into persons values('ram',10);
insert into persons values('sam',30);

select cname,clanguage,cid from country cross join persons;

select cname,clanguage,cid,pname from country inner join persons

on country.cid=persons.pnumber;

select pname,pnumber,cname from persons inner join country

on persons.pnumber=country.cid;

select cname,clanguage,cid,pname,pnumber from country left outer join persons

on country.cid=persons.pnumber;


select cname,clanguage,cid from country right outer join persons

on country.cid=persons.pnumber;


select cname,clanguage,cid,pname,pnumber from country full outer join persons

on country.cid=persons.pnumber;

select c.cname,c.clanguage,c.cid,p.pname,p.pnumber from country as c,persons as p

where c.cid=p.pnumber;

select c.cname as cname,c.cid as cid,pname from country as c,persons as p


where c.cid = p.pnumber;

truncate table country;

select * from country;

begin;
delete from country where cname='china';
rollback;
commit;
 select * from country where cid in(select cid from country where cid>10);
 

update country set cid=5 * cid where cid in(select cid from country where cid>5 );

delete from country where cid in(select cid from country where cid=150);
