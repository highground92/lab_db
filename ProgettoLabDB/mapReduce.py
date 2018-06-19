# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 16:43:06 2018

@author: Fabio
"""
from bson.code import Code
from pymongo import MongoClient
import os
import glob

def get_all_dataSet():
    owd= os.getcwd()
    os.chdir(owd+"/dataSet/")
    dataset_list=[]
    for file in glob.glob('*.txt'):
        dataset_list.append(file)
    return dataset_list

def open_connection_to_mongo():
    client = MongoClient('localhost', 27017)
    db = client['dbTweetProva']
    collection = db['tweet_dict']
    return collection

<<<<<<< HEAD
client = MongoClient('localhost', 27017)
db = client['dbTweetProva']
collection = db['tweet_dict']

dataset_list=get_all_dataSet()

=======
collection = open_connection_to_mongo()
>>>>>>> Stefano

map = Code("function() {emit(this.word+' : '+this.sentiment,1);};")
reduce = Code("function(word,count) {return Array.sum(count);};")
result = collection.map_reduce(map, reduce, "words_frequency")

