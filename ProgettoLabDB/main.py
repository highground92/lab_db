# -*- coding: utf-8 -*-
import os
import glob
import labDBSA
import wordsCloud
import oracleDB
import mongoDB
from pymongo import MongoClient

def get_all_dataSet():
    owd= os.getcwd()
    os.chdir(owd+"/dataSet/")
    dataset_list=[]
    for file in glob.glob('*.txt'):
        dataset_list.append(file)
    return dataset_list

def open_connection_to_mongo():
    client = MongoClient('localhost', 27017)
    db = client['dbTweet']
    collection = db['tweet_dict']
    return collection

def find_sentiment(file):
    return file[8:-4]

count = 0
startDir=os.getcwd()
lexical_resources = labDBSA.get_lexical_resources()
collection = open_connection_to_mongo()
        
dataset_list=get_all_dataSet()
owd= os.getcwd()
parentDir=os.path.abspath(os.path.join(owd, os.pardir))


#Lettura di tutti i dataset, trattamento e caricamento su mongo e Oracle
for file in dataset_list :    
    with open(file, 'r', encoding='utf-8') as myfile:
        data=myfile.read().replace('\n', '')
        wordsFiltered = labDBSA.run_clean_tweet(data,parentDir)
        words_dict = labDBSA.createDictionary(wordsFiltered,lexical_resources)
        #caricamento su Oracle
        oracleDB.connessioneOracle(words_dict,wordsFiltered,file)
        #caricamento su Mongo
        count = mongoDB.caricamentoMongo(wordsFiltered,file,count,collection)
        os.chdir(startDir)       
        sentiment=find_sentiment(file)
        wordsCloud.create_word_cloud(sentiment,wordsFiltered)
        os.chdir("/Users/stevi/.spyder-py3/ProgettoLabDB/dataSet/")

mongoDB.mapReduce(collection)
