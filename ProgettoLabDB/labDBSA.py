# -*- coding: utf-8 -*-

from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from collections import defaultdict
from resources import emoji_list, punctuation_mark, slang_words, pos
import collections
import glob
import json
import csv
import emoji
import os

def char_is_emoji(character):
    return character in emoji.UNICODE_EMOJI

def text_has_emoji(text):
    for character in text:
        if character in emoji.UNICODE_EMOJI:
            return True
    return False

#TODO: gestire le parole "nuove" non presenti nelle risorse lessicali ????????
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

#Leggo ogni risorsa lessicale presente 
def get_lexical_resources():
    sentiment_list = search_dir('resources')
    owd = os.getcwd()
    lexical_dictionary = defaultdict()
    for dir in sentiment_list:
        os.chdir(owd+"/resources/"+dir)
        resources_dictionary = defaultdict()
        for file in glob.glob('*.csv'):
            csv_dict = defaultdict()
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
 
#Leggo il dataSet e lo metto come stringa  TODO:Generalizzare la lettura del file
with open(os.path.abspath("dataSet/dataset_dt_joy_60k.txt"), 'r', encoding='utf-8') as myfile:
    data=myfile.read().replace('\n', '') 

#Creazione del file senza stopWords
stopWords = set(stopwords.words('english'))
words = TweetTokenizer().tokenize(data)
wordsFiltered = [] 
for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)

#Levo USERNAME e URL
deleteWords = ['USERNAME', 'URL']
wordsFiltered = [h for h in wordsFiltered if h not in deleteWords]

#Riconosco gli hashtags        
hashtags=[h for h in wordsFiltered if h.startswith("#")]
wordsFiltered=[h for h in wordsFiltered if not h.startswith("#")]
                                                            
#Emoji       
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

#Punteggiatura
wordsFiltered=[h for h in wordsFiltered if h not in punctuation_mark.punctuation]

#Lowercase
wordsFiltered=[h.lower() for h in wordsFiltered]

#Slang
slangWords=[h for h in wordsFiltered if h in slang_words.slang]
wordsFiltered=[h for h in wordsFiltered if h not in slang_words.slang]

#POS tagging
posTagging=[h for h in wordsFiltered if h in pos.tag]
wordsFiltered=[h for h in wordsFiltered if h not in pos.tag]

#Stemming
ps = PorterStemmer()
wordsFiltered=[ps.stem(h) for h in wordsFiltered]

#Conteggio parole
dictionaryWordsCount= collections.Counter(wordsFiltered)

"""
print("STAMPO VALORI: ")
print("countEmoPos: "+repr(countEmoPos))
print("countEmoNeg: "+repr(countEmoNeg))
print("countEmoNeut: "+repr(countEmoNeut))
print("countPosEmoticons: "+repr(countPosEmoticons))
print("countNegEmoticons: "+repr(countNegEmoticons))"""
           
""" 
print("LISTA HASHTAGS: ")            
print(hashtags)    
print("LISTA SLANG: ")
print(slangWords)
print("LISTA POS TAG: ")
print(posTagging)
print("DIZIONARIO PAROLE-COUNT: ")
print(dictionaryWordsCount)    
#Stampo risultato 
print("TWEET PULITI: ")    
print(wordsFiltered)"""


#leggo i nomi dei sentimenti e delle risorse
lexical_resources = get_lexical_resources()

words_dict = process_dataSets(wordsFiltered,lexical_resources)

print('//////////////')
print('//////////////')
with open('words_dict.txt', 'w') as file:
     file.write(json.dumps(words_dict))
"""     
print('LEXICAL RESOURCES:')
for w in lexical_resources:
    print('sentiment:' + w)
    for r in lexical_resources[w]:
        print(r)"""

        
