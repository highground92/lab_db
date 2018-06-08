# -*- coding: utf-8 -*-

import os
import csv
import glob
from collections import defaultdict

def search_dir(directory):
    dirList = next(os.walk(directory))[1]
    return [h for h in dirList if not h.find("__")!=-1]

csv_dict = defaultdict()

with open(os.path.abspath("resources/con-score/afinn.txt"), 'r') as f:
    reader = csv.reader(f,delimiter='\t')
    for row in reader:
        csv_dict[row[0]] = row[1]
        

def get_lexical_resources():
    sentiment_list = search_dir('resources')
    owd = os.getcwd()
    lexical_dictionary = defaultdict()
    for dir in sentiment_list:
        os.chdir(owd+"/resources/"+dir)
        resources_dictionary = defaultdict()
        for file in glob.glob('*.csv'):
            csv_dict = defaultdict()
            print('csv: ' + file)
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

new_dictionary = get_lexical_resources()
print(new_dictionary['neg']['listNegEffTerms'])


