# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:05:44 2018

@author: Fabio
"""

import cx_Oracle

con = cx_Oracle.connect('labdb1718/root@127.0.0.1/xe')
print (con.version)

cur = con.cursor()
"""
try:
    cur.execute("INSERT INTO words_dict VALUES ('parola2','sentimento',1,0,1)")
    con.commit()
except:
    print('ROLLOOOO')
    con.rollback()

print(cur)
"""
cur.execute("select * from words_dict WHERE word='pupu'")
row = cur.fetchall()
print (row)
    
cur.close()
con.close()
