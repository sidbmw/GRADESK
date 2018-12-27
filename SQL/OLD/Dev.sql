SELECT * FROM eom_class 
ORDER BY year, class;

SELECT * FROM eom_students
ORDER BY student_id;

SELECT * FROM eom_marks
ORDER BY student_id, task, expectation;

SELECT class,  first_name, last_name, colour, task, expectation, mark, comments, anomaly, deleted_flag
FROM eom_students, eom_marks
WHERE eom_students.student_id = eom_marks.student_id
--AND deleted_flag = 'N'
ORDER BY class, first_name, last_name, task, expectation;