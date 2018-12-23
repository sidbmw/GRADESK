--------------------------------------------------------
--  File created - Saturday-December-22-2018   
--------------------------------------------------------
REM INSERTING into EOM.EOM_MARKS
DROP TABLE eom_marks;
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

SET DEFINE OFF;
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (1,'blue','T2','A3','3+',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (1,'blue','T1','C3','3+/4-',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (1,'blue','T2','C1','3+/4-',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (1,'blue','Q2','B2','4',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (1,'blue','T3','B2','4',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (1,'blue','T1','A1','4++',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (1,'blue','T2','B4','4/4+',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (1,'blue','T1','B2','4/4+',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (1,'blue','Q1','B2','4/4+',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (2,'blue','T1','A1','1+','Was sick. Retest offered.','Y','Y');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (2,'blue','T1','B2','2-',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (2,'blue','T1','C3','3',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (2,'blue','T2','B4','3--',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (2,'blue','T2','A3','4++',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (2,'blue','T1','A1','4++',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (2,'blue','T2','C1','R',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (3,'blue','T1','A1','3+',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (3,'blue','T1','C3','3+/4-',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (3,'blue','T2','B4','3--',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (3,'blue','T2','B1','4++',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (3,'blue','T2','A3','4++',null,'N','N');
Insert into EOM.EOM_MARKS (STUDENT_ID,COLOUR,TASK,EXPECTATION,MARK,COMMENTS,ANOMALY,DELETED_FLAG) values (3,'blue','T1','B2','4++',null,'N','N');

drop table eom_main_screen_layout;

CREATE TABLE eom_main_screen_layout (
    student_id    NUMBER NOT NULL,
    expectation   VARCHAR(2) NOT NULL,
    seq_no        NUMBER NOT NULL,
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
    x3s3p         VARCHAR(2),
    x_3p          VARCHAR(2),
    x_3ps4m       VARCHAR(2),
    x_4m          VARCHAR(2),
    x_4ms4        VARCHAR(2),
    x_4           VARCHAR(2),
    x4s4p         VARCHAR(2),
    x_4p          VARCHAR(2),
    x_4pp         VARCHAR(2)
);