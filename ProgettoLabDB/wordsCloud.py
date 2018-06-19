# -*- coding: utf-8 -*-
import os
import glob
from os import path
from PIL import Image
import numpy as np
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
    dirList = next(os.walk(os.getcwd()))[1]
    return [h for h in dirList if h.find(sentiment)!=-1]

#Trasformo wordsFiltered in testo per la word cloud
def get_file(wordsFiltered,fileName):
<<<<<<< HEAD
    with open(fileName+'.txt', 'w+') as modFile:
        for w in wordsFiltered:
            modFile.write(w+"\n")
=======
    with open(fileName+'.txt','w+') as modFile:
        for w in wordsFiltered:
            modFile.write(w+'\n')
>>>>>>> Fabio
    return modFile

#Creao la word cloud del dataset wordsfiltered
def create_word_cloud(fileName,wordsFiltered):
    dirProject=os.getcwd()
<<<<<<< HEAD
    f=get_file(wordsFiltered,fileName)    
=======
    f=get_file(wordsFiltered,fileName)
>>>>>>> Fabio
    create_WC(f.name,dirProject,fileName)
    
#Wrapper di create_word_cloud
def create_WC(fileFiltered,dirProject,fileName):
<<<<<<< HEAD

    text=open(path.join(dirProject, fileFiltered)).read()        
=======
    text=open(path.join(dirProject, fileFiltered)).read()
>>>>>>> Fabio
    
    for h in get_image_sentiment(fileName,dirProject):
        emoji_colored= np.array(Image.open(path.join(h, fileName+".png")))
        os.chdir(dirProject)
        wc = WordCloud(background_color="white", max_words=5000, mask=emoji_colored,
<<<<<<< HEAD
                       max_font_size=40, random_state=42,contour_width=1,contour_color='gray')
=======
                       max_font_size=40, random_state=42, contour_width=1, contour_color='gray')
>>>>>>> Fabio

        #Genera la word cloud
        wc.generate(text)

        #Crea il colore dall'immagine
        image_colors = ImageColorGenerator(emoji_colored)
<<<<<<< HEAD
        """
=======
        
        """"
>>>>>>> Fabio
        #Colorazione immagine e stampa,da commentare
        #plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
        #plt.axis("off") 
        #plt.figure() 
<<<<<<< HEAD
        """
=======
        # fin qui
        """
        
>>>>>>> Fabio
        wc.recolor(color_func=image_colors)
        os.chdir(dirProject+"/wordsCloudImg")        
        wc.to_file(fileName+".png")
        os.chdir(dirProject)
<<<<<<< HEAD
=======
        
>>>>>>> Fabio
