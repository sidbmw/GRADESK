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
column X_R format a7 heading 'INC'
column X_1MM format a7 heading '1--'
column X_1MS1 format a7 heading '1-/1'
column X_1 format a7 heading '   1   '
column X_1S1P format a7 heading '1/1+'
column X_1P format a7 heading '1+'
column X_1PS2M format a7 heading '1+/2-'
column X_2M format a7 heading '2-'
column X_2MS2 format a7 heading '2-/2'
column X_2 format a7 heading '2'
column X_2S2P format a7 heading '2/2+'
column X_2P format a7 heading '2+'
column X_2PS3M format a7 heading '2+/3-'
column X_3M format a7 heading '3-'
column X_3MS3 format a7 heading '3-/3'
column X_3 format a7 heading '3'
column X_3S3P format a7 heading '3/3+'
column X_3P format a7 heading '3+'
column X_3PS4M format a7 heading '3+/4-'
column X_4M format a7 heading '4-'
column X_4MS4 format a7 heading '4-/4'
column X_4 format a7 heading '4'
column X_4S4P format a7 heading '4/4+'
column X_4P format a7 heading '4+'
column X_4PP format a7 heading '4++'

select expectation, X_R, X_1MM, X_1MS1, X_1, X_1S1P, X_1P, X_1PS2M, X_2M, X_2MS2, X_2, X_2S2P, X_2P, X_2PS3M, X_3M, X_3MS3, X_3, X_3S3P, X_3P, X_3PS4M, X_4M, X_4MS4, X_4, X_4S4P, X_4P, X_4PP
from   eom_main_screen_layout
order by expectation;

exit

    