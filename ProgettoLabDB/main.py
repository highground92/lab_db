# -*- coding: utf-8 -*-
import os
import glob
import labDBSA
import wordsCloud
import oracleDB
<<<<<<< HEAD
import mongoDB

=======
import json
from pymongo import MongoClient
from collections import defaultdict
>>>>>>> Stefano

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

def find_sentiment(file):
    return file[8:-4]


startDir=os.getcwd()
lexical_resources = labDBSA.get_lexical_resources()
collection = open_connection_to_mongo()
           
dataset_list=get_all_dataSet()
owd= os.getcwd()
parentDir=os.path.abspath(os.path.join(owd, os.pardir))
<<<<<<< HEAD
print(parentDir)
count = 0

=======


#Lettura di tutti i dataset, trattamento e caricamento su mongo e Oracle
>>>>>>> Stefano
for file in dataset_list :    
    with open(file, 'r', encoding='utf-8') as myfile:
        data=myfile.read().replace('\n', '')
        wordsFiltered = labDBSA.run_clean_tweet(data,parentDir)
<<<<<<< HEAD
        words_dict = labDBSA.createDictionary(wordsFiltered)
        #caricamento su Oracle
        #oracleDB.connessioneOracle(words_dict,wordsFiltered,file)
        #caricamento su Mongo
        collection = mongoDB.connessioneMongo(wordsFiltered,file,count)
        count = mongoDB.caricamentoMongo(wordsFiltered,file,count,collection)
        mongoDB.mapReduce(collection)
        owd= os.getcwd()
        os.chdir(owd+"/dataSet/")
        
=======
        words_dict = labDBSA.createDictionary(wordsFiltered,lexical_resources)
        #insert_words_in_mongo(wordsFiltered,0)
        os.chdir("words_dict")
        create_wordsdict(file,words_dict)
        os.chdir(startDir)       
        sentiment=find_sentiment(file)
        wordsCloud.create_word_cloud(sentiment,wordsFiltered)
        owd= os.getcwd()        
        os.chdir(owd+"/dataSet/")
    

#oracleDB.connessioneOracle(words_dict, wordsFiltered)    
>>>>>>> Stefano
