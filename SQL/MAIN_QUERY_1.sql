select * from eom_marks where student_id=1 and mark in ('4/4+','4');

select x_4s4p.expectation, x_4s4p.task x_4s4p, x_4.task x_4
from  eom_marks x_4s4p,
      eom_marks x_4
where x_4s4p.student_id=1
and   x_4s4p.mark='4/4+'
--
and  x_4.student_id(+)=1
and  x_4.mark(+)='4'
order by 1,2;

select x_4s4p.expectation,  x_4s4p.task x_4s4p
from  eom_marks x_4s4p
where x_4s4p.student_id=1
and   x_4s4p.mark='4/4+';

select x_4.expectation,  x_4.task x_4
from  eom_marks x_4
where   x_4.student_id(+)=1
and  x_4.mark(+)='4'

