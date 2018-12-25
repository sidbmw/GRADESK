begin
    FOR r_exp IN (select distinct expectation from eom_marks where student_id=1)
    LOOP
        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_INC)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = 'INC';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_R)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = 'R';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_1MM)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '1--';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_1MS1)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '1-/1';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_1)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '1';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_1S1P)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '1/1+';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_1P)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '1+';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, x_1ps2m)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '1+/2-';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_2M)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '2-';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_2MS2)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '2-/2';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_2)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '2';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_2S2P)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '2/2+';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_2P)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '2+';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_2PS3M)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '2+/3-';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_3M)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '3-';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_3MS3)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '3-/3';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_3)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '3';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_3S3P)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '3/3+';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_3P)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '3+';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_3PS4M)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '3+/4-';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_4M)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '4-';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_4MS4)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '4-/4';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_4)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '4';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_4S4P)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '4/4+';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_4P)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '4+';

        INSERT INTO eom_main_screen_layout (STUDENT_ID, EXPECTATION, X_4PP)
        SELECT STUDENT_ID, EXPECTATION, TASK
        FROM EOM_MARKS WHERE STUDENT_ID = 1 AND EXPECTATION = r_exp.expectation AND MARK = '4++';

    END LOOP;
    --assign seq_no on the layout table for each student_id, expectation

    FOR r_exp IN (
        SELECT DISTINCT
            expectation
        FROM
            eom_main_screen_layout
        WHERE
            student_id = 1
    ) LOOP
        UPDATE eom_main_screen_layout
        SET
            seq_no = ROWNUM
        WHERE
            student_id = 1
            AND expectation = r_exp.expectation;

    END LOOP;


end;/
