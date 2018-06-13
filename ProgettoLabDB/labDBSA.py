# -*- coding: utf-8 -*-
 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from collections import defaultdict
import os
import emoji_list
import glob
import csv
import string

# -*- encoding: utf-8 -*-
# pip install emoji

import emoji


def char_is_emoji(character):
    return character in emoji.UNICODE_EMOJI


def text_has_emoji(text):
    for character in text:
        if character in emoji.UNICODE_EMOJI:
            return True
    return False

#TODO: gestire le parole "nuove" non presenti nelle risorse lessicali
def process_dataSets(filtered_words,lexical_resources):
    new_dict = defaultdict()
    for w in wordsFiltered:
        sentiment_dict = defaultdict()
        for l in lexical_resources:
            resources_dict = defaultdict()
            presence_count = 0
            for res_name in lexical_resources[l]:
                if w in lexical_resources[l][res_name]:
                    resources_dict[res_name] = 1
                    presence_count += 1
                else:
                    resources_dict[res_name] = 0
            resources_dict['lexical_res_presence'] = presence_count
            resources_dict['lexical_res_frequency'] = presence_count/len(lexical_resources[l])
            sentiment_dict[l] = resources_dict
        new_dict[w] = sentiment_dict
    return new_dict
    

def search_dir(directory):
    dirList = next(os.walk(directory))[1]
    return [h for h in dirList if not h.find("__")!=-1]

def get_lexical_resources():
    sentiment_list = search_dir('resources')
    owd = os.getcwd()
    lexical_dictionary = defaultdict()
    for dir in sentiment_list:
        os.chdir(owd+"/resources/"+dir)
        resources_dictionary = defaultdict()
        for file in glob.glob('*.csv'):
            csv_dict = defaultdict()
            print('csv: ' + file)
            with open(os.getcwd()+'/'+file, 'r') as f:
                reader = csv.reader(f,delimiter='\t')
                for row in reader:
                    csv_dict[row[0]] = row[1]
            resources_dictionary[file[:-4]] = csv_dict
        for file in glob.glob('*.tsv'):
            csv_dict = defaultdict()     
            with open(os.getcwd()+'/'+file, 'r') as f:
                reader = csv.reader(f,delimiter='\t')
                for row in reader:
                    csv_dict[row[0]] = row[1]
            resources_dictionary[file[:-4]] = csv_dict
        for file in glob.glob("*.txt"):
            if file == 'afinn.txt':
                csv_dict = defaultdict()     
                with open(os.getcwd()+'/'+file, 'r') as f:
                    reader = csv.reader(f,delimiter='\t')
                    for row in reader:
                        csv_dict[row[0]] = row[1]
                resources_dictionary[file[:-4]] = csv_dict
            else:
                res = open(os.getcwd()+'/'+file, 'r', encoding='utf-8')
                resources_dictionary[file[:-4]] = res.read().splitlines()
        lexical_dictionary[dir] = resources_dictionary
    os.chdir(owd)
    return lexical_dictionary
 
#Leggo il dataSet e lo metto come stringa
with open(os.path.abspath("dataSet/dataset_joy_piccolo.txt"), 'r', encoding='utf-8') as myfile:
    data=myfile.read().replace('\n', '') 

#Levo le stopWords, TODO mettere le stopWords della prof, spostare questo piú avanti
stopWords = set(stopwords.words('english'))
words = TweetTokenizer().tokenize(data)
wordsFiltered = [] #File filtrato
for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)

#Levo USERNAME e URL
deleteWords = ['USERNAME', 'URL']
wordsFiltered = [h for h in wordsFiltered if h not in deleteWords]

#Processo hashtags.
hashtags = []
#Metodo precedente quando ogni elemento era tokenizzato come parola
"""hashSymbol= ['#']
for index, h in enumerate(list(wordsFiltered)):
    if h in hashSymbol:
        nxt=wordsFiltered.index(h)
        value=wordsFiltered[nxt+1]
        hashtags.append(value)
        wordsFiltered.remove(h)
        wordsFiltered.remove(value)"""
#for index, h in enumerate(list(wordsFiltered)):
for h in wordsFiltered:
    if h.startswith("#"):
        #print("H inizia con "+h)            
        hashtags.append(h)
        wordsFiltered.remove(h)
        
hashtags=[h for h in wordsFiltered if h.startswith("#")]
wordsFiltered=[h for h in wordsFiltered if not h.startswith("#")]
                                                            
#Emoji.             
countEmoPos=len([h for h in wordsFiltered if h in set(emoji_list.EmojiPos)])
wordsFiltered=[h for h in wordsFiltered if h not in set(emoji_list.EmojiPos)]

countEmoNeg=len([h for h in wordsFiltered if h in set(emoji_list.EmojiNeg)])
wordsFiltered=[h for h in wordsFiltered if h not in set(emoji_list.EmojiNeg)]

countEmoNeut=len([h for h in wordsFiltered if h in set(emoji_list.OthersEmoji)])
wordsFiltered=[h for h in wordsFiltered if h not in set(emoji_list.OthersEmoji)]

#Emoticons
countPosEmoticons=len([h for h in wordsFiltered if h in set(emoji_list.posemoticons)])
wordsFiltered=[h for h in wordsFiltered if h not in set(emoji_list.posemoticons)]

countNegEmoticons=len([h for h in wordsFiltered if h in set(emoji_list.negemoticons)])
wordsFiltered=[h for h in wordsFiltered if h not in set(emoji_list.negemoticons)]


print("STAMPO VALORI: ")
print("countEmoPos: "+repr(countEmoPos))
print("countEmoNeg: "+repr(countEmoNeg))
print("countEmoNeut: "+repr(countEmoNeut))
print("countPosEmoticons: "+repr(countPosEmoticons))
print("countNegEmoticons: "+repr(countNegEmoticons))

#lista delle emoji con nome (es :flushed_face:) e codice utf8
"""
print('Lista Emoji tradotte')
for w in wordsFiltered:
    if text_has_emoji(w):
        print(emoji.demojize(w))
        print(w.encode(encoding='utf-8'))
        #print(w.decode('unicode-escape').encode('latin1').decode('utf8'))
"""

#leggo i nomi dei sentimenti e delle risorse
lexical_resources = get_lexical_resources()

words_dict = process_dataSets(wordsFiltered,lexical_resources)
print('//////////////')
print('//////////////')
#with open('words_dict.txt', 'w') as file:
#     file.write(json.dumps(words_dict))
print('LEXICAL RESOURCES:')
for w in lexical_resources:
    print('sentiment:' + w)
    for r in lexical_resources[w]:
        print(r)

"""
from pymongo import MongoClient

# Create connection to MongoDB
client = MongoClient('localhost', 27017)
db = client['database_di_prova']
collection = db['words_dict_prova']

# Build a basic dictionary

# Insert the dictionary into Mongo
collection.insert(words_dict)
print('done')
"""

import cx_Oracle

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
