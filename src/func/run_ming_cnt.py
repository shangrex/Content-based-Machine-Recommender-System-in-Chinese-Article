import spacy
from spacy.lang.zh.examples import sentences 
import argparse
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from tqdm import tqdm

def ming_recommend(txt, topk=50):

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

    for i in range(topk):
        print(rst[i][0][0][0])
        print(rst[i][1:])


    return rst[:topk]