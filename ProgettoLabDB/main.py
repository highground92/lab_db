# -*- coding: utf-8 -*-
import os
import glob
import labDBSA
import cx_Oracle
def get_all_dataSet():
    owd= os.getcwd()
    os.chdir(owd+"/dataSet/")
    dataset_list=[]
    for file in glob.glob('*.txt'):
        dataset_list.append(file)
    return dataset_list

dataset_list=get_all_dataSet()
owd= os.getcwd()
parentDir=os.path.abspath(os.path.join(owd, os.pardir))
print(parentDir)
for file in dataset_list :    
    with open(file, 'r', encoding='utf-8') as myfile:
        print(file)
        data=myfile.read().replace('\n', '')
        words_dict = labDBSA.run_clean_tweet(data,parentDir)
        owd= os.getcwd()
        os.chdir(owd+"/dataSet/")
        
"""
con = cx_Oracle.connect('labdb1718/root@127.0.0.1/xe')
cur = con.cursor()
for word in words_dict:
    query = "insert into JOY values ('"+word+"',"+repr(words_dict[word]["joy"]["EmoSN_joy"])+","+repr(words_dict[word]["joy"]["NRC_joy"])+","+repr(words_dict[word]["joy"]["sentisense_joy"])+","+repr(words_dict[word]["joy"]["lexical_res_presence"])+","+repr(words_dict[word]["joy"]["lexical_res_frequency"])+")"
    print(query)
    try:
        cur.execute(query)
        con.commit()
    except:
        print('rollback')
        con.rollback()
cur.close()
con.close()
"""