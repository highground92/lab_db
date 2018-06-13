# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:19:48 2018

@author: Giulia
"""

""" CONNESSIONE AL DB ORACLE """

import cx_Oracle
import labDBSA

def connessioneOracle(words_dict, wordsFiltered) :
    con = cx_Oracle.connect('labDB1718/root@127.0.0.1')
    print(con.version)
    cur = con.cursor()
    
    words_count = labDBSA.countCurrency(wordsFiltered)
    
    for w in words_dict :
        for s in words_dict[w] :
            if(words_dict[w][s]['lexical_res_presence'] != 0) :
                if(s == 'anger') :
                    rows = [ (''+w, words_dict[w][s]['EmoSN_anger'], words_dict[w][s]['NRC_anger'], words_dict[w][s]['sentisense_anger'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into anger (word, emosn, nrc, sentisense, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6)",rows)
                    con.commit()
                if(s == 'anticipation') :
                    rows = [ (''+w, words_dict[w][s]['NRC_anticipation'], words_dict[w][s]['sentisense_anticipation'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into anticipation (word, nrc, sentisense, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5)",rows)
                    con.commit()
                if(s == 'con-score') :
                    rows = [ (''+w, words_dict[w][s]['afinn'], words_dict[w][s]['anewAro_tab'], words_dict[w][s]['anewDom_tab'], words_dict[w][s]['anewPleas_tab'], words_dict[w][s]['Dal_Activ'], words_dict[w][s]['Dal_Imag'], words_dict[w][s]['Dal_Pleas'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into conscore (word, afinn, anewaro, anewdom, anewpleas, dal_activ, dal_imag, dal_pleas, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10)",rows)
                    con.commit()
                if(s == 'disgust-hate') :
                    rows = [ (''+w, words_dict[w][s]['NRC_disgust'], words_dict[w][s]['sentisense_disgust'], words_dict[w][s]['sentisense_hate'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into disgust_hate (word, nrc, sentisense_disgust, sentisense_hate, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6)",rows)
                    con.commit()
                if(s == 'fear') :
                    rows = [ (''+w, words_dict[w][s]['NRC_fear'], words_dict[w][s]['sentisense_fear'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into fear (word, nrc, sentisense, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5)",rows)
                    con.commit()
                if(s == 'hope') :
                    rows = [ (''+w, words_dict[w][s]['sentisense_hope'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into hope (word, sentisense, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4)",rows)
                    con.commit()
                if(s == 'joy') :
                    rows = [ (''+w, words_dict[w][s]['EmoSN_joy'], words_dict[w][s]['NRC_joy'], words_dict[w][s]['sentisense_joy'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into joy (word, emosn, nrc, sentisense, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6)",rows)
                    con.commit()
                if(s == 'like-love') :
                    rows = [ (''+w, words_dict[w][s]['sentisense_like'], words_dict[w][s]['sentisense_love'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into like_love (word, sentisense_like, sentisense_love, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5)",rows)
                    con.commit()
                if(s == 'neg') :
                    rows = [ (''+w, words_dict[w][s]['GI_NEG'], words_dict[w][s]['HL-negatives'], words_dict[w][s]['listNegEffTerms'], words_dict[w][s]['LIWC-NEG'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into neg (word, gi, hl, listnegeffterms, liwc, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6, :7)",rows)
                    con.commit()
                if(s == 'pos') :
                    rows = [ (''+w, words_dict[w][s]['GI_POS'], words_dict[w][s]['HL-positives'], words_dict[w][s]['listPosEffTerms'], words_dict[w][s]['LIWC-POS'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into pos (word, gi, hl, listposeffterms, liwc, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5, :6, :7)",rows)
                    con.commit()    
                if(s == 'sadness') :
                    rows = [ (''+w, words_dict[w][s]['NRC_sadness'], words_dict[w][s]['sentisense_sadness'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into sadness (word, nrc, sentisense, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5)",rows)
                    con.commit()
                if(s == 'surprise') :
                    rows = [ (''+w, words_dict[w][s]['NRC_surprise'], words_dict[w][s]['sentisense_surprise'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into surprise (word, nrc, sentisense, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4, :5)",rows)
                    con.commit()
                if(s == 'trust') :
                    rows = [ (''+w, words_dict[w][s]['NRC_trust'], words_count[w], words_dict[w][s]['lexical_res_frequency']) ]
                    cur.executemany("insert into trust (word, nrc, frequency_dataset, lexical_res_frequency) values (:1, :2, :3, :4)",rows)
                    con.commit()
            else :
                if(s == 'newword') :
                    rows = [ (''+w, ''+s, words_count[w]) ]
                    cur.executemany("insert into newword (word, res, frequency) values (:1, :2, :3)",rows)
                    con.commit()                    
    cur.close()
    con.close()
    return