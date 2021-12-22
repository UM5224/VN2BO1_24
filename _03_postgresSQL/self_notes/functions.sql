CREATE TABLE  agents(
  id1 int,
   name1 varchar(10),
    area1 varchar(10),
   country1 varchar(10)
	 );
	 
	
INSERT INTO AGENTS VALUES (10, 'Ramasundar', 'Bangalore', 'india');
INSERT INTO AGENTS VALUES (20, 'Alex ', 'London', 'england');
INSERT INTO AGENTS VALUES (30, 'Alford', 'New York', 'us');
INSERT INTO AGENTS VALUES (40, 'Ravi Kumar', 'coloumbo', 'lanka');

select * from agents

create function sum()
returns int as $$
declare 
       total integer;
begin
	select count(*) into total from agents;
    return total;
end;
$$ language plpgsql;

select sum();