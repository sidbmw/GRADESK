import cx_Oracle
import PySimpleGUI as sg
import pandas as pd
import sys

con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
cur = con.cursor(scrollable=True)

sql = "UPDATE EOM_CLASS SET CLASS = 'TMJ4M-55' WHERE CLASS = 'ICS4U-08'"

cur.execute(sql)

con.commit()

print(cur.rowcount, "record(s) affected")
