import pandas as pd
import pickle
import random


def ming_cls():
    x = random.randint(0, 5)
    y = random.randint(0, 5)

    rst1 = []
    f = open(f'data/pretrain/spa_ming_emb_cls{x}.pkl', 'rb')
    spa_emb = pickle.load(f)

    for i in range(5):
        rst1.append(random.choice(spa_emb)[:3])

    f.close()
    rst2 = []
    f = open(f'data/pretrain/spa_ming_emb_cls{y}.pkl', 'rb')
    spa_emb = pickle.load(f)

    for i in range(5):
        rst2.append(random.choice(spa_emb)[:3])
    f.close()

    return [rst1, rst2]
