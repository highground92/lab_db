# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import os
import glob
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, ImageColorGenerator

def get_image_sentiment(sentiment,pathPar):
    os.chdir(pathPar+"/resources/Image/")
    for img in glob.glob('*'+sentiment+'*'):
        name=img
    os.chdir(pathPar+"/words_dict")
    return name


def create_word_cloud(sentimentName,wordsFiltered):
    progettoDir=os.getcwd()
    create_WC(wordsFiltered,progettoDir,sentimentName)
    
#Per ogni sentimento creo la words cloud
def create_WC(wordsFiltered,progettoDir,sentimentName):
    
    #pathImage= path.dirname('resources/Image/')
        #print(text)
    image=get_image_sentiment(sentimentName,progettoDir)
    #emoji_colored= np.array(Image.open(image[0]))
    emoji_colored= np.array(Image.open(path.join(os.chdir(progettoDir+"/resources/Image/"),get_image_sentiment(sentimentName,progettoDir))))
    
    wc = WordCloud(background_color="white", max_words=2000, mask=emoji_colored,
                           max_font_size=40, random_state=42)
            
            #Genera la word cloud
    wc.generate(wordsFiltered)
    
            #Crea il colore dall'immagine
    image_colors = ImageColorGenerator(emoji_colored)
    
            #Colorazione immagine e stampa,da commentare
    plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off") 
    plt.figure() 
            # fin qui
        
    os.chdir(progettoDir+"/wordsCloudImg")        
    wc.to_file(sentimentName+".png")
    os.chdir(progettoDir)
        
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
