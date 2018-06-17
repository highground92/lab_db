# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 16:43:06 2018

@author: Fabio
"""
from bson.code import Code
from pymongo import MongoClient

def open_connection_to_mongo():
    client = MongoClient('localhost', 27017)
    db = client['dbTweetProva']
    collection = db['tweet_dict']
    return collection

collection = open_connection_to_mongo()

map = Code("function() {emit(this.word,1);};")
reduce = Code("function(word,count) {return Array.sum(count);};")
result = collection.map_reduce(map, reduce, "words_frequency")

