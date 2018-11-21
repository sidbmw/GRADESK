# https://stackoverflow.com/questions/43565189/get-column-value-by-name-rather-than-position-in-cx-oracle

from __future__ import print_function

import cx_Oracle
import collections

# import dbconfig

con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
cur = con.cursor(scrollable=True)

cur.execute("select * from EOM_CLASS")

for row in cur:
    # print(row)
    # print(row[0])
    # print(row[1])
    v_class = row[0]
    print(v_class)

    print("record fetch completed")
