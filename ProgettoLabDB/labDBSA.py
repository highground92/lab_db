# -*- coding: utf-8 -*-
from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from collections import defaultdict
from resources import emoji_list, punctuation_mark, slang_words, pos
import collections
import glob
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

def process_dataSets(wordsFiltered,lexical_resources):
    print("- Datasets")
    new_dict = defaultdict()
    for w in wordsFiltered:
        sentiment_dict = defaultdict()
        for l in lexical_resources:
            resources_dict = defaultdict()
            presence_count = 0
            for res_name in lexical_resources[l]:
                if w in lexical_resources[l][res_name]:
                    presence_count += 1
                    if l == 'con-score':
                        resources_dict[res_name] = lexical_resources[l][res_name][w]
                    else:
                        resources_dict[res_name] = 1
                else:
                    resources_dict[res_name] = 0
            resources_dict['lexical_res_presence'] = presence_count
            if(len(lexical_resources[l])!=0) :
                resources_dict['lexical_res_frequency'] = presence_count/len(lexical_resources[l])
            sentiment_dict[l] = resources_dict
        new_dict[w] = sentiment_dict
    return new_dict
    
def get_all_dir(directory):
    dirList = next(os.walk(directory))[1]
    return [h for h in dirList if not h.find("__")!=-1]

#Leggo ogni risorsa lessicale presente 
def get_lexical_resources():
    sentiment_list = get_all_dir('resources')
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

def countCurrency(wordsFiltered) :
    dictionaryWordsCount= collections.Counter(wordsFiltered)
    return dictionaryWordsCount

def createDictionary(wordsFiltered,lexical_resources):
    words_dict = process_dataSets(wordsFiltered,lexical_resources)
    return words_dict

#Metodo principale di trattamento dei tweets
def run_clean_tweet(data, parentDir):
    
    os.chdir(parentDir)
    
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
                                                                                                                                                                               #Emoji       emoji.UNICODE_EMOJI
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
    
    #Rimozione delle non parole
    wordsFiltered=[h for h in wordsFiltered if h.isalpha()]
    
    """
    #Scrivo il file per le words cloud
    nameFile=''
    f= open(nameFile,"w+")
    for item in wordsFiltered:
        f.write("%s\n" % item)"""
    #print(wordsFiltered)
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
    print(wordsFiltered)
    """
    """         
    print('LEXICAL RESOURCES:')
    for w in lexical_resources:
        print('sentiment:' + w)
        for r in lexical_resources[w]:
            print(r)"""      
    return wordsFiltered





