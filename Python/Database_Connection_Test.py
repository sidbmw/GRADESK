# myscript.py

from __future__ import print_function

import cx_Oracle

con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
print (con.version)
con.close()