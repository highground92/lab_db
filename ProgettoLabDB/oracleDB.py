# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:19:48 2018

@author: Giulia
"""

""" CONNESSIONE AL DB ORACLE """

import cx_Oracle

con = cx_Oracle.connect('labDB1718/root@127.0.0.1')
print(con.version)
cur = con.cursor()

rows = [ ('girll', 0, 0, 0, 2, 0.0) ]
cur.executemany("insert into anger(word, emosn, nrc, sentisense, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6)", rows)
con.commit()

cur2 = con.cursor()
cur2.execute("select * from anger")
res = cur2.fetchall()
print(res)

cur2.close()
cur.close()
con.close()
