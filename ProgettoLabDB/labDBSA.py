# -*- coding: utf-8 -*-

from nltk.stem import PorterStemmer 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import os
from resources import emoji_list, punctuation_mark, slang_words, pos
import re 
import collections

#Leggo il dataSet e lo metto come stringa
with open(os.path.abspath("dataSet/dataset_joy_piccolo.txt"), 'r') as myfile:
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
print(wordsFiltered)