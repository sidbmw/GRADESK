create or replace procedure eom_student_sort is 

    v_sort_id   NUMBER:= 1;
BEGIN

    FOR r_std IN (
        SELECT
            class,
            last_name,
            first_name,
            ROWID
        FROM
            eom_students
        ORDER BY
            class,
            last_name,
            first_name
    ) LOOP
        UPDATE eom_students
        SET
            sort_id = v_sort_id
        WHERE
            rowid = r_std.rowid;

        v_sort_id := v_sort_id + 1;
    END LOOP;

END eom_student_sort;
/



SELECT * FROM EOM_STUDENTS ORDER BY CLASS, LAST_NAME, FIRST_NAME;