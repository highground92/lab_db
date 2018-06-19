# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:19:48 2018

@author: Giulia
"""

""" CONNESSIONE AL DB ORACLE """
import os
import cx_Oracle
import labDBSA

#gestione caratteri speciali
os.environ["NLS_LANG"] = ".UTF8"

def connessioneOracle(words_dict, wordsFiltered,dataset) :
    con = cx_Oracle.connect('labDB1718/root@127.0.0.1')
    print("- Save data in DB Oracle for tweet "+dataset)
    cur = con.cursor()
    
    words_count = labDBSA.countCurrency(wordsFiltered)
    
    for w in words_dict :
        flag = 0
        for s in words_dict[w] :
            if(words_dict[w][s]['lexical_res_presence'] != 0) :
                if(s == 'anger') :
                    rows = [ (''+dataset, ''+w, words_dict[w][s]['EmoSN_anger'], words_dict[w][s]['NRC_anger'], words_dict[w][s]['sentisense_anger'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into anger (dataset, word, emosn, nrc, sentisense, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6, :7)",rows)
                    con.commit()
                if(s == 'anticipation') :
                    rows = [ (''+dataset, ''+w, words_dict[w][s]['NRC_anticipation'], words_dict[w][s]['sentisense_anticipation'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into anticipation (dataset, word, nrc, sentisense, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6)",rows)
                    con.commit()
                if(s == 'con-score') :
                    rows = [ (''+dataset, ''+w, words_dict[w][s]['afinn'], words_dict[w][s]['anewAro_tab'], words_dict[w][s]['anewDom_tab'], words_dict[w][s]['anewPleas_tab'], words_dict[w][s]['Dal_Activ'], words_dict[w][s]['Dal_Imag'], words_dict[w][s]['Dal_Pleas'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into conscore (dataset, word, afinn, anewaro, anewdom, anewpleas, dal_activ, dal_imag, dal_pleas, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)",rows)
                    con.commit()
                if(s == 'disgust-hate') :
                    rows = [ (''+dataset, ''+w, words_dict[w][s]['NRC_disgust'], words_dict[w][s]['sentisense_disgust'], words_dict[w][s]['sentisense_hate'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into disgust_hate (dataset, word, nrc, sentisense_disgust, sentisense_hate, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6, :7)",rows)
                    con.commit()
                if(s == 'fear') :
                    rows = [ (''+dataset, ''+w, words_dict[w][s]['NRC_fear'], words_dict[w][s]['sentisense_fear'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into fear (dataset, word, nrc, sentisense, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6)",rows)
                    con.commit()
                if(s == 'hope') :
                    rows = [ (''+dataset, ''+w, words_dict[w][s]['sentisense_hope'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into hope (dataset, word, sentisense, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5)",rows)
                    con.commit()
                if(s == 'joy') :
                    rows = [ (''+dataset, ''+w, words_dict[w][s]['EmoSN_joy'], words_dict[w][s]['NRC_joy'], words_dict[w][s]['sentisense_joy'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into joy (dataset, word, emosn, nrc, sentisense, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6, :7)",rows)
                    con.commit()
                if(s == 'like-love') :
                    rows = [ (''+dataset, ''+w, words_dict[w][s]['sentisense_like'], words_dict[w][s]['sentisense_love'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into like_love (dataset, word, sentisense_like, sentisense_love, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6)",rows)
                    con.commit()
                if(s == 'neg') :
                    rows = [ (''+dataset, ''+w, words_dict[w][s]['GI_NEG'], words_dict[w][s]['HL-negatives'], words_dict[w][s]['listNegEffTerms'], words_dict[w][s]['LIWC-NEG'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into neg (dataset, word, gi, hl, listnegeffterms, liwc, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6, :7, :8)",rows)
                    con.commit()
                if(s == 'pos') :
                    rows = [ (''+dataset, ''+w, words_dict[w][s]['GI_POS'], words_dict[w][s]['HL-positives'], words_dict[w][s]['listPosEffTerms'], words_dict[w][s]['LIWC-POS'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into pos (dataset, word, gi, hl, listposeffterms, liwc, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6, :7, :8)",rows)
                    con.commit()    
                if(s == 'sadness') :
                    rows = [ (''+dataset, ''+w, words_dict[w][s]['NRC_sadness'], words_dict[w][s]['sentisense_sadness'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into sadness (dataset, word, nrc, sentisense, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6)",rows)
                    con.commit()
                if(s == 'surprise') :
                    rows = [ (''+dataset, ''+w, words_dict[w][s]['NRC_surprise'], words_dict[w][s]['sentisense_surprise'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into surprise (dataset, word, nrc, sentisense, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6)",rows)
                    con.commit()
                if(s == 'trust') :
                    rows = [ (''+dataset, ''+w, words_dict[w][s]['NRC_trust'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into trust (dataset, word, nrc, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5)",rows)
                    con.commit()
            else :
                if(flag==0) :
                    rows = [ (''+dataset, ''+w, words_count[w]) ]
                    cur.executemany("insert into newword (dataset, word, frequency) values (:1, :2, :3)",rows)
                    con.commit()
                    flag=1
                                        
    cur.close()
    con.close()
    return