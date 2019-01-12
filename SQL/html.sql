set markup html on spool on PREFORMAT OFF -
TABLE "WIDTH='100%' BORDER='5'"
set feedback off



ALTER SESSION SET NLS_DATE_FORMAT = 'DD-Mon-YYYY hh24:mi:ss';
set heading off
set termout off
COLUMN SYSDATE NEW_VALUE report_date

SELECT SYSDATE FROM DUAL;

spool C:\Users\siddh\Documents\ICS4U\Reports\report.htm



TTITLE CENTER 'STUDENT REPORT' RIGHT 'Date: ' report_date


set heading off
select  'Student Name :  ' || last_name ||', ' || first_name "Student Name"
from eom_students
where student_id = (select distinct student_id from eom_main_screen_layout);


ttitle off

set heading on
column expectation format a11 heading 'Expectation'
column X_inc format a7 heading 'INC'
column X_R format a7 heading 'R'
column X_1M format a7 heading '1-'
--column X_1MS1 format a7 heading '1-/1'
column X_1 format a7 heading '   1   '
--column X_1S1P format a7 heading '1/1+'
column X_1P format a7 heading '1+'
--column X_1PS2M format a7 heading '1+/2-'
column X_2M format a7 heading '2-'
--column X_2MS2 format a7 heading '2-/2'
column X_2 format a7 heading '2'
--column X_2S2P format a7 heading '2/2+'
column X_2P format a7 heading '2+'
--column X_2PS3M format a7 heading '2+/3-'
column X_3M format a7 heading '3-'
--column X_3MS3 format a7 heading '3-/3'
column X_3 format a7 heading '3'
--column X_3S3P format a7 heading '3/3+'
column X_3P format a7 heading '3+'
column X_3PS4M format a7 heading '3+/4-'
column X_4M format a7 heading '4-'
column X_4MS4 format a7 heading '4-/4'
column X_4 format a7 heading '4'
column X_4S4P format a7 heading '4/4+'
column X_4P format a7 heading '4+'
column X_4PP format a7 heading '4++'

select expectation, x_inc, x_r, x_1m, x_1, x_1p, x_2m, x_2, x_2p, x_3m, x_3, x_3p, x_3ps4m, x_4m, x_4ms4, x_4, x_4s4p, x_4p, x_4pp
from   eom_main_screen_layout
order by expectation;

exit

    