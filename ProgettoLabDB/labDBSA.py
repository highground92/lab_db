# -*- coding: utf-8 -*-

from nltk.stem import PorterStemmer 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from collections import defaultdict
import os
<<<<<<< HEAD
#<<<<<<< HEAD
from resources import emoji_list, punctuation_mark, slang_words, pos
import re 
import collections



=======
import emoji_list
import glob
import json
import csv
>>>>>>> Fabio

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
            for res_name in lexical_resources[l]:
                if w in lexical_resources[l][res_name]:
                    resources_dict[res_name] = 1
                else:
                    resources_dict[res_name] = 0
            sentiment_dict[l] = resources_dict
        new_dict[w] = sentiment_dict
    return new_dict
    

<<<<<<< HEAD

=======
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
>>>>>>> Fabio
 
#>>>>>>> Fabio
#Leggo il dataSet e lo metto come stringa
with open(os.path.abspath("dataSet/dataset_dt_joy_60k.txt"), 'r', encoding='utf-8') as myfile:
    data=myfile.read().replace('\n', '') 

#Creazione del file senza stopWords
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
"""for h in wordsFiltered:
    if h.startswith("#"):
        #print("H inizia con "+h)            
        hashtags.append(h)
        wordsFiltered.remove(h)"""
        
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
Per prendere il valore di una data chiave(e quindi parola)
dict = {'Name': 'Zabra', 'Age': 7}
print "Value : %s" %  dict.get('Age')
print "Value : %s" %  dict.get('Education', "Never")
"""

print("STAMPO VALORI: ")
print("countEmoPos: "+repr(countEmoPos))
print("countEmoNeg: "+repr(countEmoNeg))
print("countEmoNeut: "+repr(countEmoNeut))
print("countPosEmoticons: "+repr(countPosEmoticons))
print("countNegEmoticons: "+repr(countNegEmoticons))
<<<<<<< HEAD
            
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
#<<<<<<< HEAD
print(wordsFiltered)


#print(sentenceFiltered)
=======
>>>>>>> Fabio

#lista delle emoji con nome (es :flushed_face:) e codice utf8
"""
print('Lista Emoji tradotte')
for w in wordsFiltered:
    if text_has_emoji(w):
        print(emoji.demojize(w))
        print(w.encode(encoding='utf-8'))
        #print(w.decode('unicode-escape').encode('latin1').decode('utf8'))
<<<<<<< HEAD
  
#Prova caricamento risorse lessicali relative a joy
with open(os.path.abspath("resources/joy/EmoSN_joy.txt"), 'r', encoding='utf-8') as joyFile:
    EmoSN_joy=joyFile.read().splitlines()
with open(os.path.abspath("resources/joy/NRC_joy.txt"), 'r', encoding='utf-8') as joyFile:
    NRC_joy=joyFile.read().splitlines()
with open(os.path.abspath("resources/joy/sentisense_joy.txt"), 'r', encoding='utf-8') as joyFile:
    sentisense_joy=joyFile.read().splitlines()

#Creazione dei dictionary delle risorse lessicali joy
EmoSN_joy_dict = defaultdict()
NRC_joy_dict = defaultdict()
sentisense_joy_dict = defaultdict()

for w in EmoSN_joy:
    EmoSN_joy_dict[w]=w
for w in NRC_joy:
    NRC_joy_dict[w] = w
for w in sentisense_joy:
    sentisense_joy_dict[w]=w
        
#creazione primo dictionary con chiavi le parole filtrate:
new_words_dict = defaultdict()

joy_dict = process_joy_resourcesB(wordsFiltered,new_words_dict)

print('///////////')
print('JOY WORDS DICTIONARY:')
print(joy_dict)
print('NEW JOY WORDS:')
print(new_words_dict)
print('conteggio WORDS:')
        
#>>>>>>> Fabio
=======
"""

#leggo i nomi dei sentimenti e delle risorse
lexical_resources = get_lexical_resources()

words_dict = process_dataSets(wordsFiltered,lexical_resources)
print('//////////////')
print('//////////////')
with open('words_dict.txt', 'w') as file:
     file.write(json.dumps(words_dict))
print('LEXICAL RESOURCES:')
for w in lexical_resources:
    print('sentiment:' + w)
    for r in lexical_resources[w]:
        print(r)

        
>>>>>>> Fabio
