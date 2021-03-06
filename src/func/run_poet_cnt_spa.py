'''
Use Spacy (Word Embedding) to Recommend Poet
'''
import spacy
from spacy.lang.zh.examples import sentences 
from sklearn.metrics.pairwise import cosine_similarity
import argparse
import pandas as pd
import numpy as np
import pickle
from tqdm import tqdm


nlp = spacy.load("zh_core_web_lg")
nlp.enable_pipe("senter")


def poet_cnt(txt, topk=200):
    f = open(f'data/pretrain/spa_embedding.pkl', 'rb')
    spa_emb = pickle.load(f)

    poet = pd.read_csv('data/poet.csv')
    doc = nlp(txt)

    tmp_v = doc.vector
    rst = []

    for i in tqdm(range(len(spa_emb))):
        ftmp = cosine_similarity([spa_emb[i][3]], [tmp_v])
        if ftmp < 0.3:
            continue
        rst.append([ftmp[0][0], poet['title'].iloc[i], poet['author'].iloc[i], poet['paragraphs'].iloc[i]])


    rst = sorted(rst, key=lambda i : i[0], reverse=True)


    cnt_rst = {}
    for i in range(topk):
        if rst[i][1] in cnt_rst:
            cnt_rst[rst[i][1]+'-'+rst[i][2]] += 1
        else:
            cnt_rst[rst[i][1]+'-'+rst[i][2]] = 1
            
    cnt_rst = sorted(cnt_rst.items(), key=lambda i: i[1], reverse=True)

    rst=[]
    for i in cnt_rst:
        print(i)
        rst.append(i[0])
        
    return rst[:50]