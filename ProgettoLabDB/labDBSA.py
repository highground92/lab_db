# -*- coding: utf-8 -*-
 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from collections import defaultdict
import os


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

import emoji_list
 
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
        print("H inizia con "+h)            
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
            
print("LISTA HASHTAGS: ")            
print(hashtags)    
    
#Stampo risultato 
print("TWEET PULITI: ")    
print(wordsFiltered)
#print(sentenceFiltered)

#lista delle emoji con nome (es :flushed_face:) e codice utf8
print('Lista Emoji tradotte')
for w in wordsFiltered:
    if text_has_emoji(w):
        print(emoji.demojize(w))
        print(w.encode(encoding='utf-8'))
        #print(w.decode('unicode-escape').encode('latin1').decode('utf8'))

#Prova creazione dizionari annidati
myDict = defaultdict()
myDict2 = defaultdict()
myDict2["prova"] = 2
myDict['home'] = myDict2
print(myDict["home"]["prova"])
  # {'home': {'state': 'MN'}}
  
#prova caricamento EmoSN_anger in dictionary
with open(os.path.abspath("resources/EmoSN_anger.txt"), 'r', encoding='utf-8') as angerFile:
    dataAnger=angerFile.read()
wordsAnger = dataAnger.splitlines()
print(wordsAnger)

angerDict = defaultdict()

for w in wordsAnger:
    angerDict[w]=w

print('prova di stampa')
print(angerDict['caste'])
        
        