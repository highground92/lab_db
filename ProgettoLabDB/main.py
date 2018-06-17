# -*- coding: utf-8 -*-
import os
import glob
import labDBSA
import wordsCloud
import oracleDB
import json
from pymongo import MongoClient
from collections import defaultdict

def get_all_dataSet():
    owd= os.getcwd()
    os.chdir(owd+"/dataSet/")
    dataset_list=[]
    for file in glob.glob('*.txt'):
        dataset_list.append(file)
    return dataset_list

def insert_words_in_mongo(wordsFiltered,count):
    for w in wordsFiltered:
        mongo_word = defaultdict()
        mongo_word['sentiment'] = file[:-4]
        mongo_word['_id'] = count
        mongo_word['word'] = w
        count = count+1
        collection.insert_one(mongo_word)

def open_connection_to_mongo():
    client = MongoClient('localhost', 27017)
    db = client['dbTweetProva']
    collection = db['tweet_dict']
    return collection
 
def create_wordsdict(file,words_dict):             
    with open('words_dict_'+file[:-4]+'.txt', 'w') as file:
         file.write(json.dumps(words_dict))
         
collection = open_connection_to_mongo()
           
dataset_list=get_all_dataSet()
owd= os.getcwd()
parentDir=os.path.abspath(os.path.join(owd, os.pardir))

#Lettura di tutti i dataset, trattamento e caricamento su mongo e Oracle
for file in dataset_list :    
    with open(file, 'r', encoding='utf-8') as myfile:
        data=myfile.read().replace('\n', '')
        wordsFiltered = labDBSA.run_clean_tweet(data,parentDir)
        words_dict = labDBSA.createDictionary(wordsFiltered)
        insert_words_in_mongo(wordsFiltered,0)
        create_wordsdict(file,words_dict,file)
        wordsCloud.create_word_cloud()
        owd= os.getcwd()        
        os.chdir(owd+"/dataSet/")
    

#oracleDB.connessioneOracle(words_dict, wordsFiltered)    
