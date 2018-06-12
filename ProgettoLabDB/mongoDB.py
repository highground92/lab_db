# -*- coding: utf-8 -*-

from pymongo import MongoClient

# Create connection to MongoDB
client = MongoClient('localhost', 27017)
db = client['database_di_prova']
collection = db['collection_di_prova']

# Build a basic dictionary
#d = {'website': 'www.carrefax.com', 'author': 'Daniel Hoadley', 'colour': 'purple'}

# Insert the dictionary into Mongo
#collection.insert(d)