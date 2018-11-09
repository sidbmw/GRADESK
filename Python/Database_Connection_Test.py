# myscript.py

from __future__ import print_function

import cx_Oracle

con = cx_Oracle.connect('EOM@//localhost:1521/xe')
print (con.version)
con.close()