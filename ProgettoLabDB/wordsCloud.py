# -*- coding: utf-8 -*-
import os
import glob
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, ImageColorGenerator

def get_all_words_dict(pathPar):
    owd= os.getcwd()
    os.chdir(owd+"/words_dict/")
    wordsdict_list=[]
    for file in glob.glob('*.txt'):
        wordsdict_list.append(file)
    return wordsdict_list

def get_image_sentiment(sentiment,pathPar):
    os.chdir(pathPar+"/resources/Image/")
    image_list=[]
    for img in glob.glob('*'+sentiment+'*'):
        image_list.append[img]
    os.chdir(pathPar+"/words_dict")
    return image_list


#Prendo tutti i file per ogni sentimento
def create_word_cloud():
    progettoDir=os.getcwd()
    all_words_dict=get_all_words_dict(progettoDir)
    create_WC(all_words_dict,progettoDir)
    
#Per ogni sentimento creo la words cloud
def create_WC(all_words_dict,progettoDir):
    
    #pathImage= path.dirname('resources/Image/')
    for h in all_words_dict:
        text = open(h,"r").read()
    
        sentiment = h[:-4]
        
        for h in get_image_sentiment(sentiment,progettoDir):
            emoji_colored= np.array(Image.open(h))
        
        wc = WordCloud(background_color="white", max_words=2000, mask=emoji_colored,
                       max_font_size=40, random_state=42)
    
        #Genera la word cloud
        wc.generate(text)
    
        #Crea il colore dall'immagine
        image_colors = ImageColorGenerator(emoji_colored)
    
        #Colorazione immagine e stampa
        plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
        plt.axis("off")
        plt.figure()
        
        wc.to_file("wordSmile"+sentiment+".png")

"""Per dare ad ogni gruppo di parole un colore specifico (nel caso volessimo metterle tutte assieme)
https://github.com/amueller/word_cloud/blob/master/examples/colored_by_group.py

color_to_words = {
    # words below will be colored with a green single color function
    '#00ff00': ['beautiful', 'explicit', 'simple', 'sparse',
                'readability', 'rules', 'practicality',
                'explicitly', 'one', 'now', 'easy', 'obvious', 'better'],
    # will be colored with a red single color function
    'red': ['ugly', 'implicit', 'complex', 'complicated', 'nested',
            'dense', 'special', 'errors', 'silently', 'ambiguity',
            'guess', 'hard']
}
"""