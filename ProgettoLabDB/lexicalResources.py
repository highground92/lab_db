# -*- coding: utf-8 -*-

import glob, os
import string
from nltk.tokenize import word_tokenize

def clean_resource_file(file):
    return[h for h in file if h.find("_")==-1]
            
def detokenize_file(file):
    return "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in file]).strip()    

def create_file_clean(name,file):
    f= open("2"+name,"w+")
    f.write(detokenize_file(file))
    f.close()
    
def search_dir(directory):
    dirList = next(os.walk(directory))[1]
    return [h for h in dirList if not h.find("__")!=-1]



for dir in search_dir("resources"):
    os.chdir("resources/"+dir)
    for file in glob.glob("*.txt"):
        with open(file, 'r', encoding='utf-8') as myfile:
            data=myfile.read()
            tmpFile = word_tokenize(data)
            newFile=clean_resource_file(tmpFile)
            create_file_clean(file,newFile)
        
        
    

