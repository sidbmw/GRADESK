DROP TABLE eom_class;
DROP TABLE eom_students;
DROP TABLE eom_marks;
DROP SEQUENCE eom_students_s;

CREATE TABLE eom_class
(
  class      VARCHAR2(15) NOT NULL,
  period_num INTEGER      NOT NULL
);

CREATE UNIQUE INDEX eom_class_U1 ON eom_class (class, year, period_num);

CREATE TABLE eom_students
(
  student_id NUMBER       NOT NULL,
  class      VARCHAR2(15) NOT NULL,
  first_name VARCHAR2(50) NOT NULL,
  last_name  VARCHAR2(50) NOT NULL
);



CREATE TABLE eom_marks
(
  student_id   NUMBER       NOT NULL,
  colour       VARCHAR2(20) NOT NULL,
  task         VARCHAR(2)   NOT NULL,
  expectation  VARCHAR2(2)  NOT NULL,
  mark         VARCHAR2(5)  NOT NULL,
  comments     VARCHAR2(250),
  anomaly      VARCHAR2(1)  NOT NULL,
  deleted_flag VARCHAR2(1)  NOT NULL
);

CREATE UNIQUE INDEX eom_marks_U1 ON eom_marks (student_id, task, expectation, deleted_flag);



INSERT INTO eom_class (class, period_num)
VALUES ('ICS4U-01/2018', '1');

INSERT INTO eom_class (class, period_num)
VALUES ('ICS4U-02/2018', '2');

INSERT INTO eom_class (class, period_num)
VALUES ('ICS4U-03/2018', '3');

INSERT INTO eom_class (class, period_num)
VALUES ('ICS4U-04/2018', '4');



INSERT INTO eom_class (class, period_num)
VALUES ('ICS4U-05/2018', '1');

INSERT INTO eom_class (class, period_num)
VALUES ('ICS4U-06/2018', '2');

INSERT INTO eom_class (class, period_num)
VALUES ('ICS4U-07/2018', '3');

INSERT INTO eom_class (class, period_num)
VALUES ('ICS4U-08/2018', '4');


INSERT INTO eom_class (class, period_num)
VALUES ('ICS4U-01/2019', '1');

INSERT INTO eom_class (class, period_num)
VALUES ('ICS4U-02/2019', '2');



CREATE SEQUENCE eom_students_s
  MINVALUE 1
  START WITH 1
  INCREMENT BY 1
  CACHE 10;

--Insert Students

--Insert Student Mike
INSERT INTO eom_students (student_id, class, first_name, last_name)
VALUES (eom_students_s.nextval, 'ICS4U-01/2018', 'Mike', 'Dong');

--Insert Marks for Mike
--Test 1
INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T1', 'A1', '4++', '', 'N', 'N');

INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T1', 'B2', '4/4+', '', 'N', 'N');

INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T1', 'C3', '3+/4-', '', 'N', 'N');

--Test 2
INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T2', 'A3', '3+', '', 'N', 'N');

INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T2', 'B4', '4/4+', '', 'N', 'N');

INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T2', 'C1', '3+/4-', '', 'N', 'N');


--Insert Student Siddharth
INSERT INTO eom_students (student_id, class, first_name, last_name)
VALUES (eom_students_s.nextval, 'ICS4U-01/2018', 'Siddharth', 'Natamai');

--Insert Marks for Siddharth
--Test1
INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T1', 'A1', '1+', 'Was sick. Retest offered.', 'Y', 'Y');

INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T1', 'A1', '4++', '', 'N', 'N');

INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T1', 'B2', '2-', '', 'N', 'N');

INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T1', 'C3', '3', '', 'N', 'N');


--Test 2
INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T2', 'A3', '4++', '', 'N', 'N');

INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T2', 'B4', '3--', '', 'N', 'N');

INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T2', 'C1', 'R', '', 'N', 'N');

--Insert Student Wade
INSERT INTO eom_students (student_id, class, first_name, last_name)
VALUES (eom_students_s.nextval, 'ICS4U-02/2018', 'Wade', 'Huang');


--Insert Marks Wade
--Test1
INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T1', 'A1', '3+', '', 'N', 'N');

INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T1', 'B2', '4++', '', 'N', 'N');

INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T1', 'C3', '3+/4-', '', 'N', 'N');


--Test 2
INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T2', 'A3', '4++', '', 'N', 'N');

INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T2', 'B4', '3--', '', 'N', 'N');

INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES (eom_students_s.currval, 'blue', 'T2', 'B1', '4++', '', 'N', 'N');
