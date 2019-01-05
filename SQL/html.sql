set markup html on spool on
set feedback off

spool C:\Users\siddh\Documents\ICS4U\Reports\report.htm
ttitle center "Student Report" skip 3

--select * from eom_main_screen_layout;

set heading off
select  'Student Name :  ' || last_name ||', ' || first_name "Student Name"
from eom_students
where student_id = (select distinct student_id from eom_main_screen_layout);

set heading on
column x_inc heading 'INC'
column x_1mm heading '1--'
select expectation, x_inc, x_r, x_1mm  
from   eom_main_screen_layout
order by expectation;

exit

    