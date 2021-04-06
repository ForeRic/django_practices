select * from emaillist;

-- scheme
desc guestbook;

-- insert
insert into guestbook values(null, '정지윤', '1234','ㅎㅇ!', now());


-- select
select 	no, 
		name, 
		message, 
        date_format(reg_date, '%Y-%m-%d %p %h:%i:%s') as reg_date
from 	guestbook 
order by reg_date desc;

-- delete
delete 
  from guestbook
where no = 1
	and password = '1234';
    
desc emaillist02_emaillist;