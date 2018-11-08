# myscript.py

from __future__ import print_function

import cx_Oracle

con = cx_Oracle.connect('EOM/EOM@localhost/orcl')
print (con.version)
con.close()