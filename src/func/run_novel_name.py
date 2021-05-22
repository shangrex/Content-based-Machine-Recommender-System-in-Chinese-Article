import spacy
from spacy.lang.zh.examples import sentences 
from sklearn.metrics.pairwise import cosine_similarity
import argparse
import pandas as pd
import numpy as np
from tqdm import tqdm
import pickle


def novel_name(txt, topk=100):

    nlp = spacy.load("zh_core_web_lg")
    nlp.enable_pipe("senter")

    nov = pd.read_csv('data/novel.csv')


    f = open(f'data/pretrain/spa_nov_emb.pkl', 'rb')
    spa_emb = pickle.load(f)


    doc = nlp(txt)

    rst = []

    for i in tqdm(range(len(nov))):
        ftmp = cosine_similarity([spa_emb[i][3]], [doc.vector])
        rst.append([ftmp, nov['name'].iloc[i], nov['author'].iloc[i], nov['paragraphs'].iloc[i]])


    rst = sorted(rst, key=lambda i : i[0], reverse=True)


    cnt_rst = {}
    for i in range(topk):
        if rst[i][1] in cnt_rst:
            cnt_rst[rst[i][1]] += 1
        else:
            cnt_rst[rst[i][1]] = 1
            
    cnt_rst = sorted(cnt_rst.items(), key=lambda i: i[1], reverse=True)

    rst = []
    for i in cnt_rst:
        print(i)
        rst.append(i)
    return rst