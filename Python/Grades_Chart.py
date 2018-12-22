import cx_Oracle
import PySimpleGUI as sg
import sys

con = cx_Oracle.connect('system/earluser@127.0.0.1/xe')
cur = con.cursor(scrollable=True)
name_ID = [[], []]

marks = [[], [[], []]]


# def do_it(class): #parameter need to be class code + year

# get the students with class, then the student ID with names, then marks with student ID
# alphabetical fetch from database
def get_class_students(class_code):
    cur.execute("select * from EOM_STUDENTS")
    for row in cur:
        if str(class_code) == str(row[1]):
            name_ID[0].append(row[2] + " " + row[3])
            name_ID[1].append(row[0])
            marks[0].append(row[0])

def get_marks(student_ID):
    cur.execute("select * from EOM_MARKS")
    for row in cur:
        if ()


get_class_students("ICS4U-01/2018")
