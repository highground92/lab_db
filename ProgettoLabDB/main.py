# -*- coding: utf-8 -*-
import os
import glob
import labDBSA
import oracleDB
import mongoDB


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
count = 0

for file in dataset_list :    
    with open(file, 'r', encoding='utf-8') as myfile:
        data=myfile.read().replace('\n', '')
        wordsFiltered = labDBSA.run_clean_tweet(data,parentDir)
        words_dict = labDBSA.createDictionary(wordsFiltered)
        #caricamento su Oracle
        #oracleDB.connessioneOracle(words_dict,wordsFiltered,file)
        #caricamento su Mongo
        collection = mongoDB.connessioneMongo(wordsFiltered,file,count)
        count = mongoDB.caricamentoMongo(wordsFiltered,file,count,collection)
        mongoDB.mapReduce(collection)
        owd= os.getcwd()
        os.chdir(owd+"/dataSet/")
        
