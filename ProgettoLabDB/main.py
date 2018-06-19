# -*- coding: utf-8 -*-
import os
import glob
import labDBSA
import oracleDB
from pymongo import MongoClient
from collections import defaultdict

# Create a function called "chunks" with two arguments, l and n:
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]


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
client = MongoClient('localhost', 27017)
db = client['DataSetPiccoli']
collection = db['tweets']
count = 0
for file in dataset_list :    
    with open(file, 'r', encoding='utf-8') as myfile:
        data=myfile.read().replace('\n', '')
        wordsFiltered = labDBSA.run_clean_tweet(data,parentDir)
        words_dict = labDBSA.createDictionary(wordsFiltered)
        #caricamento su Oracle
        oracleDB.connessioneOracle(words_dict,wordsFiltered,file)
        #caricamento su Mongo
        for w in wordsFiltered:
            mongo_word = defaultdict()
            mongo_word['sentiment'] = file[:-4]
            mongo_word['_id'] = count
            mongo_word['word'] = w
            count = count+1
            collection.insert_one(mongo_word)
        owd= os.getcwd()
        os.chdir(owd+"/dataSet/")
#    mongo_words[file[:-4]] = wordsFiltered
        

"""
client = MongoClient('localhost', 27017)
db = client['dbTweetProva']
collection = db['tweet_dict']
collection.insert_one(mongo_words)

#oracleDB.connessioneOracle(words_dict, wordsFiltered)    
"""