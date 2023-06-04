CREATE TABLE users(  
    id_user SERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    sec_name VARCHAR(255),
    last_name VARCHAR(255) NOT NULL,
    birthdate DATE NOT NULL,
    posting_date DATE NULL DEFAULT CURRENT_DATE
);

insert into users(first_name, sec_name, last_name, birthdate)
values ('Pedro', 'Antonio', 'Vázquez', '1998-12-09');

insert into users(first_name, sec_name, last_name, birthdate)
values ('Aideé', 'Berenice', 'Correa', '1997-09-03');

insert into users(first_name, last_name, birthdate)
values ('Jessica', 'Alarcón', '1997-10-24');

insert into users(first_name, sec_name, last_name, birthdate)
values ('Guillermo', 'Francisco','Contreras', '1999-02-08');

insert into users(first_name, sec_name, last_name, birthdate)
values ('Blanca', NULL, 'Rivera', '1998-11-07');

delete from users where id_user = 1;

select * from users;

select 
	first_name, 
	last_name,
	age(birthdate) as age
from 
	users;

SELECT * from users WHERE sec_name = NULL;