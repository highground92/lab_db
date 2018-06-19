# -*- coding: utf-8 -*-
from pymongo import MongoClient
from collections import defaultdict
from bson.code import Code

def connessioneMongo(wordsFiltered, dataset, count) :
    client = MongoClient('localhost', 27017)
    db = client['DataSetPiccoli']
    collection = db['tweets']
    return collection

def caricamentoMongo(wordsFiltered, dataset, count, collection) :
    for w in wordsFiltered:
        mongo_word = defaultdict()
        mongo_word['sentiment'] = dataset[:-4]
        mongo_word['_id'] = count
        mongo_word['word'] = w
        count = count+1
        collection.insert_one(mongo_word)
    return count

def mapReduce(collection) :
    map = Code("function() {emit(this.word+' : '+this.sentiment,1);};")
    reduce = Code("function(word,count) {return Array.sum(count);};")
    collection.map_reduce(map, reduce, "words_frequency")
    return
