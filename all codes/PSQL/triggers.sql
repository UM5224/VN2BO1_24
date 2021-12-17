create table sports(
sid int generated always as identity,
sname varchar(20),
scountry varchar(10),
primary key(sid));

create table sportsaudit(
id int generated always as identity,
sid varchar(20),
sname varchar(20),
changedon timestamp(20));

CREATE OR REPLACE FUNCTION log_sname_changes()  
  RETURNS TRIGGER   
  LANGUAGE PLPGSQL  
  AS  
$$  
BEGIN  
    IF NEW.sname <> OLD.sname THEN  
         INSERT INTO sportsaudit(sname,sid,changedon)  
         VALUES(OLD.sname,OLD.sid,now());
    END IF;  
RETURN NEW;  
END;  
$$  



CREATE TRIGGER sname_changes  
 BEFORE UPDATE  
 ON sports  
 FOR EACH ROW  
 EXECUTE PROCEDURE log_sname_changes();  
 
insert into sports(sname,scountry)
values('crickrt','india'),('football','england')

select * from sports

update sports set sname='vollyball' where sid=1;

select * from sportsaudit;

drop table sportsaudit
