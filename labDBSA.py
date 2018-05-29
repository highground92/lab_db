# -*- coding: utf-8 -*-
 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os
 
#Leggo il dataSet e lo metto come stringa
with open(os.path.abspath("dataSet/dataset_joy_piccolo.txt"), 'r') as myfile:
    data=myfile.read().replace('\n', '') 

#Levo le stopWords, TODO mettere le stopWords della prof
stopWords = set(stopwords.words('english'))
words = word_tokenize(data)
wordsFiltered = [] #File filtrato
 
for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)

#Levo USERNAME e URL
deleteWords = ['USERNAME', 'URL']
for word in list(wordsFiltered):  
    if word in deleteWords:
        wordsFiltered.remove(word)

#Processo hashtags
hashtags = []
hashSymbol= ['#']
for index, h in enumerate(list(wordsFiltered)):
    if h in hashSymbol:
        nxt=wordsFiltered.index(h)
        value=wordsFiltered[nxt+1]
        hashtags.append(value)
        wordsFiltered.remove(h)
        wordsFiltered.remove(value)

            
print("LISTA HASHTAGS: ")            
print(hashtags)    
    
#Stampo risultato     
print(wordsFiltered)
