# -*- coding: utf-8 -*-

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, ImageColorGenerator

pathText = path.dirname('resources/anger/')
pathImage= path.dirname('resources/Image/')

text = open(path.join(pathText, 'EmoSN_anger.txt')).read()

# http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
emoji_colored = np.array(Image.open(path.join(pathImage, "smileRainbowW.png")))

wc = WordCloud(background_color="white", max_words=2000, mask=emoji_colored,
                max_font_size=40, random_state=42)

#Genera la word cloud
wc.generate(text)

#Crea il colore dall'immagine
image_colors = ImageColorGenerator(emoji_colored)

"""Colore diverso
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()"""
#Colorazione immagine e stampa
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
wc.to_file("wordSmile.png")

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