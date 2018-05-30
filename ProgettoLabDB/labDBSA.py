# -*- coding: utf-8 -*-
 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
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
 
#Leggo il dataSet e lo metto come stringa
with open(os.path.abspath("dataSet/dataset_joy_piccolo.txt"), 'r', encoding='utf-8') as myfile:
    data=myfile.read().replace('\n', '') 

#Levo le stopWords, TODO mettere le stopWords della prof
stopWords = set(stopwords.words('english'))
words = TweetTokenizer().tokenize(data)
wordsFiltered = [] #File filtrato

for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)

#Levo USERNAME e URL
deleteWords = ['USERNAME', 'URL']
for word in list(wordsFiltered):  
    if word in deleteWords:
        wordsFiltered.remove(word)

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
        



            
print("LISTA HASHTAGS: ")            
print(hashtags)    
    
#Stampo risultato 
print("TWEET MODIFICATI: ")    
print(wordsFiltered)
#print(sentenceFiltered)

#lista delle emoji con nome (es :flushed_face:) e codice utf8
print('Lista Emoji tradotte')
for w in wordsFiltered:
    if text_has_emoji(w):
        print(emoji.demojize(w))
        print(w.encode(encoding='utf-8'))
        
        