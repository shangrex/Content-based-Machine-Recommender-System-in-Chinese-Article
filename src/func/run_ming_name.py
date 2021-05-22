import spacy
from spacy.lang.zh.examples import sentences 
from sklearn.metrics.pairwise import cosine_similarity
import argparse
import pandas as pd
import numpy as np
import pickle
from tqdm import tqdm


def ming_name(txt, topk=50):

    nlp = spacy.load("zh_core_web_lg")
    nlp.enable_pipe("senter")


    ming = pd.read_csv('data/mingyan_new.csv')



    f = open(f'data/pretrain/spa_ming_emb.pkl', 'rb')
    spa_emb = pickle.load(f)

    doc = nlp(txt)

    rst = []

    for i in tqdm(range(len(spa_emb))):
        ftmp = cosine_similarity([doc.vector], [spa_emb[i][3]])
        rst.append([ftmp, ming['paragraphs'].iloc[i], ming['author'].iloc[i], ming['name'].iloc[i]])


    rst = sorted(rst, key=lambda i : i[0], reverse=True)


    cnt_rst = {}
    for i in range(topk):
        if rst[i][2] in cnt_rst:
            cnt_rst[rst[i][2]] += 1
        else:
            cnt_rst[rst[i][2]] = 1
            
    cnt_rst = sorted(cnt_rst.items(), key=lambda i: i[1], reverse=True)

    rst = []
    for i in cnt_rst:
        print(i)
        rst.append(i[0])

    return rst[:10]