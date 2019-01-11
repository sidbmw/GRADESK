DROP table eom_main_screen_layout;

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

REM INSERTING into EOM_MAIN_SCREEN_LAYOUT
SET DEFINE OFF;
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (1,'A1',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'T1');
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (1,'A3',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'T2',null,null,null,null,null,null,null);
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (1,'B2',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'Q2',null,null,null);
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (1,'B2',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'T3',null,null,null);
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (1,'B2',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'T1',null,null);
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (1,'B2',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'Q1',null,null);
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (1,'B4',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'T2',null,null);
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (1,'C1',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'T2',null,null,null,null,null,null);
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (1,'C3',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'T1',null,null,null,null,null,null);
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (2,'A1',null,null,null,null,null,null,null,'T1',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null);
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (2,'A1',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'T1');
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (2,'A3',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'T2');
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (2,'B2',null,null,null,null,null,null,null,null,null,'T1',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null);
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (2,'C1',null,null,'T2',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null);
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (2,'C3',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'T1',null,null,null,null,null,null,null,null,null);
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (3,'A1',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'T1',null,null,null,null,null,null,null);
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (3,'A3',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'T2');
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (3,'B1',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'T2');
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (3,'B2',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'T1');
Insert into EOM_MAIN_SCREEN_LAYOUT (STUDENT_ID,EXPECTATION,SEQ_NO,X_INC,X_R,X_1MM,X_1MS1,X_1,X_1S1P,X_1P,X_1PS2M,X_2M,X_2MS2,X_2,X_2S2P,X_2P,X_2PS3M,X_3M,X_3MS3,X_3,X_3S3P,X_3P,X_3PS4M,X_4M,X_4MS4,X_4,X_4S4P,X_4P,X_4PP) values (3,'C3',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,'T1',null,null,null,null,null,null);
