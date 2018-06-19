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
    """for img in glob.glob('*'+sentiment+'*'):
        image_list.append(img)"""
    dirList = next(os.walk(os.getcwd()))[1]
    return [h for h in dirList if h.find(sentiment)!=-1]
    #os.chdir(pathPar+"/words_dict")
    #return image_list

#Trasformo wordsFiltered in testo per la word cloud
def get_file(wordsFiltered,fileName):
    f = open(fileName+'.txt', 'w') #Vengono creati bene
    for w in wordsFiltered:
        f.write("%s\n" % w) #TODO da controllare come scrive
    f.close()
    return f

#Creao la word cloud del dataset wordsfiltered
def create_word_cloud(fileName,wordsFiltered):
    dirProject=os.getcwd()
    #all_words_dict=get_all_words_dict(progettoDir)
    #fileFiltered=get_file(wordsFiltered)
    #with open('test.txt', 'r') as f: #TODO: PERCHÉ NON SCRIVEEEEEEE?
    f=get_file(wordsFiltered,fileName)
    create_WC(f.name,dirProject,fileName)
    
#Wrapper di create_word_cloud
def create_WC(fileFiltered,dirProject,fileName):
    #pathImage= path.dirname(dirProject+"/resources/Image/")
    text=open(path.join(dirProject, fileFiltered)).read()
    
    for h in get_image_sentiment(fileName,dirProject):
        #emoji_colored= np.array(Image.open(h))
        emoji_colored= np.array(Image.open(path.join(h, fileName+".png")))
        #emoji_colored = cv2.imread(h)
        os.chdir(dirProject)
        wc = WordCloud(background_color="white", max_words=5000, mask=emoji_colored,
                       max_font_size=40, random_state=42)

        #Genera la word cloud
        wc.generate(text)

        #Crea il colore dall'immagine
        image_colors = ImageColorGenerator(emoji_colored)
    
        #Colorazione immagine e stampa,da commentare
        #plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
        #plt.axis("off") 
        #plt.figure() 
        # fin qui
        wc.recolor(color_func=image_colors)
        os.chdir(dirProject+"/wordsCloudImg")        
        wc.to_file(fileName+".png")
        os.chdir(dirProject)
        
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