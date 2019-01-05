set markup html on spool on 
set feedback off

spool C:\Users\siddh\Documents\ICS4U\Reports\report.htm

--select * from eom_main_screen_layout;

set heading off
select  'Student Name :  ' || last_name ||', ' || first_name "Student Name"
from eom_students
where student_id = (select distinct student_id from eom_main_screen_layout);

set heading on
select expectation, x_inc "INC", x_r "R", x_1mm "1--" 
from   eom_main_screen_layout
order by expectation;

exit

    