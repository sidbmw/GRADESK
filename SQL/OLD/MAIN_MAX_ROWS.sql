SELECT * FROM EOM_MARKS;
SELECT DISTINCT TASK FROM EOM_MARKS;

SELECT * FROM EOM_MARKS WHERE student_id = 1 AND expectation = 'B2';

SELECT
    mark,
    COUNT(*)
FROM
    eom_marks
WHERE
    student_id = 1
    AND expectation = 'B2'
GROUP BY
    mark;

SELECT max(max_rows)
FROM (
SELECT MARK, COUNT(*) max_rows
FROM EOM_MARKS 
WHERE student_id = 1 
AND expectation = 'B2' 
GROUP BY MARK);

-----------------------------------------------------------------

SELECT expectation, max(max_rows)
FROM
(
SELECT
    expectation,
    mark,
    COUNT(*) max_rows
FROM
    eom_marks
WHERE
    student_id = 1
    --AND expectation = 'B2'
GROUP BY
    expectation,
    mark
ORDER BY expectation)
GROUP BY EXPECTATION
order by expectation;

----------------------------------------------------

select sum(max_rows)
FROM (
SELECT expectation, max(max_rows) max_rows
FROM
(
SELECT
    expectation,
    mark,
    COUNT(*) max_rows
FROM
    eom_marks
WHERE
    student_id = 1
    --AND expectation = 'B2'
GROUP BY
    expectation,
    mark
ORDER BY expectation)
GROUP BY EXPECTATION
order by expectation);