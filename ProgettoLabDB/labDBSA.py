# -*- coding: utf-8 -*-
 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import os
import emoji
 
#Leggo il dataSet e lo metto come stringa
with open(os.path.abspath("dataSet/dataset_joy_piccolo.txt"), 'r') as myfile:
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
for h in wordsFiltered:
    if h.startswith("#"):
        hashtags.append(h)
        wordsFiltered.remove(h)
        h=0

#Emoji. TODO  capire perché non leva tutto 
print("EMOJI POS:")
print(emoji.EmojiPos)
countEmoPos = 0
countEmoNeg = 0
countEmoNeut = 0
for h in wordsFiltered:
    for j in emoji.EmojiPos:
        if h==j:
            countEmoPos += 1
            wordsFiltered.remove(h)
    for k in emoji.EmojiNeg:
        if h==k:
            countEmoNeg += 1
            wordsFiltered.remove(h)
    for l in emoji.OthersEmoji:
        if h==l:
            countEmoNeut += 1
            wordsFiltered.remove(h)

#Emoticons
countPosEmoticons = 0
countNegEmoticons = 0
for h in wordsFiltered:
    for j in emoji.posemoticons:
        if h == j:
            countPosEmoticons +=1
            wordsFiltered.remove(h)
    for k in emoji.negemoticons:
        if h == k:
            countNegEmoticons +=1
            wordsFiltered.remove(h)

#print("FACCIA CHE RIDE LINGUA FUORI")
print(emoji.EmojiPos[20]==wordsFiltered[18])
#print(wordsFiltered[18])
print("STAMPO VALORI: ")
print("countEmoPos: "+repr(countEmoPos))
print("countEmoNeg: "+repr(countEmoNeg))
print("countEmoNeut: "+repr(countEmoNeut))
print("countPosEmoticons: "+repr(countPosEmoticons))
print("countNegEmoticons: "+repr(countNegEmoticons))
            
print("LISTA HASHTAGS: ")            
print(hashtags)    
    
#Stampo risultato 
print("TWEET MODIFICATI: ")    
print(wordsFiltered)
#print(sentenceFiltered)