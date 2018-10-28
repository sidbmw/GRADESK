DROP TABLE eom_class;
DROP TABLE eom_students;
DROP TABLE eom_marks;
DROP SEQUENCE seq_person;

CREATE TABLE eom_class (
    class        VARCHAR2(10) NOT NULL,
    year         INTEGER NOT NULL,
    period_num   INTEGER NOT NULL
);

CREATE UNIQUE INDEX eom_class_U1 ON eom_class(class, year, period_num);





CREATE TABLE eom_students (
    student_id   NUMBER NOT NULL,
    class        VARCHAR2(10) NOT NULL,
    first_name   VARCHAR2(50) NOT NULL,
    last_name    VARCHAR2(50) NOT NULL
);




CREATE TABLE eom_marks (
    student_id     NUMBER NOT NULL,
    colour         VARCHAR2(20) NOT NULL,
    task           VARCHAR(2) NOT NULL,
    expectation    VARCHAR2(2) NOT NULL,
    mark           VARCHAR2(5) NOT NULL,
    comments        VARCHAR2(250),
    anomaly        VARCHAR2(1) NOT NULL,
    deleted_flag   VARCHAR2(1) NOT NULL
);

CREATE UNIQUE INDEX eom_marks_U1 ON eom_marks(student_id, task, expectation, deleted_flag);



INSERT INTO eom_class (class, year, period_num)
VALUES ('ICS4U-01', '2018', '1');

INSERT INTO eom_class (class, year, period_num)
VALUES ('ICS4U-02', '2018', '2');

INSERT INTO eom_class (class, year, period_num)
VALUES ('ICS4U-03', '2018', '3');

INSERT INTO eom_class (class, year, period_num)
VALUES ('ICS4U-04', '2018', '4');



INSERT INTO eom_class (class, year, period_num)
VALUES ('ICS4U-05', '2018', '1');

INSERT INTO eom_class (class, year, period_num)
VALUES ('ICS4U-06', '2018', '2');

INSERT INTO eom_class (class, year, period_num)
VALUES ('ICS4U-07', '2018', '3');

INSERT INTO eom_class (class, year, period_num)
VALUES ('ICS4U-08', '2018', '4');


INSERT INTO eom_class (class, year, period_num)
VALUES ('ICS4U-01', '2019', '1');

INSERT INTO eom_class (class, year, period_num)
VALUES ('ICS4U-02', '2019', '2');





    
CREATE SEQUENCE seq_person
MINVALUE 1
START WITH 1
INCREMENT BY 1
CACHE 10;

INSERT INTO eom_students (student_id, class, first_name, last_name)
VALUES (seq_person.nextval, 'ICS4U-01', 'Mike','Dong');
        
INSERT INTO eom_students (student_id, class, first_name, last_name)
VALUES (seq_person.nextval, 'ICS4U-01', 'Siddharth','Natamai');
        
INSERT INTO eom_students (student_id, class, first_name, last_name)
VALUES (seq_person.nextval, 'ICS4U-02', 'Wade','Huang');



INSERT INTO eom_marks (student_id, colour, task, expectation, mark, comments, anomaly, deleted_flag)
VALUES ('1', 'blue', 'T1', 'A1', '4++','', 'N', 'N');








SELECT * FROM eom_class;