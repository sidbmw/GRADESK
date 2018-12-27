DROP TABLE eom_class;
DROP TABLE eom_students;
DROP TABLE eom_marks;
DROP TABLE eom_main_screen_layout;
DROP SEQUENCE eom_students_s;
DROP SEQUENCE eom_main_screen_layout_s;

CREATE TABLE eom_class
(
  class      VARCHAR2(15) NOT NULL,
  period_num INTEGER      NOT NULL
);

CREATE UNIQUE INDEX eom_class_U1 ON eom_class (class, period_num);

CREATE TABLE eom_students
(
  student_id NUMBER       NOT NULL,
  class      VARCHAR2(15) NOT NULL,
  first_name VARCHAR2(50) NOT NULL,
  last_name  VARCHAR2(50) NOT NULL,
  sort_id    NUMBER       
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

CREATE SEQUENCE eom_students_s
  MINVALUE 1
  START WITH 1
  INCREMENT BY 1
  CACHE 10;


CREATE TABLE eom_main_screen_layout (
    student_id    NUMBER NOT NULL,
    expectation   VARCHAR(2) NOT NULL,
    seq_no        NUMBER,
    x_inc         VARCHAR(2),
    x_r           VARCHAR(2),
    x_1mm         VARCHAR(2), -- 1--
    x_1ms1        VARCHAR(2), --1-/1--
    x_1           VARCHAR(2), --1-- 
    x_1s1p        VARCHAR(2), --1/1+--
    x_1p          VARCHAR(2), --1+--
    x_1ps2m       VARCHAR(2), --1+/2--
    x_2m          VARCHAR(2),
    x_2ms2        VARCHAR(2),
    x_2           VARCHAR(2),
    x_2s2p        VARCHAR(2),
    x_2p          VARCHAR(2),
    x_2ps3m       VARCHAR(2),
    x_3m          VARCHAR(2),
    x_3ms3        VARCHAR(2),
    x_3           VARCHAR(2),
    x_3s3p        VARCHAR(2),
    x_3p          VARCHAR(2),
    x_3ps4m       VARCHAR(2),
    x_4m          VARCHAR(2),
    x_4ms4        VARCHAR(2),
    x_4           VARCHAR(2),
    x_4s4p        VARCHAR(2),
    x_4p          VARCHAR(2),
    x_4pp         VARCHAR(2)
);

CREATE SEQUENCE eom_main_screen_layout_s
  MINVALUE 1
  START WITH 1
  INCREMENT BY 1
  CACHE 10;

