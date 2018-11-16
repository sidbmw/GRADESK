
from __future__ import print_function

import cx_Oracle
import db_config

con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
cur = con.cursor(scrollable = True)

cur.execute("select * from dept order by deptno")

cur.scroll(2, mode = "absolute")  # go to second row
print(cur.fetchone())

cur.scroll(-1)                    # go back one row
print(cur.fetchone())