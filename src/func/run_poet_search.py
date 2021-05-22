'''
Implement a search engine.
'''
import pickle
from tqdm import tqdm
import pandas as pd 
import argparse


def poet_search(find: list, min_count=1):
    '''
    find: the word for searching
    min: the threshold of match count
    '''


    target = find.split(' ')

    poet = pd.read_csv('data/poet.csv')

    rst = []

    rst_atr = []
    rst_tit = []
    rst_cnt = []


    for i in tqdm(range(len(poet))):
        check_count = 0
        for t in target:
            if poet['author'].iloc[i] == t:
                rst_atr.append([poet['cat_paragraphs'].iloc[i] ,poet['author'].iloc[i], poet['title'].iloc[i], poet['tags'].iloc[i]])
            if type(poet['title'].iloc[i]) == float:
                continue
            if t in poet['title'].iloc[i]:
                rst_tit.append([poet['cat_paragraphs'].iloc[i] ,poet['author'].iloc[i], poet['title'].iloc[i], poet['tags'].iloc[i]])

            if t in poet['cat_paragraphs'].iloc[i]:
                check_count += 1
        if check_count > 0:
            rst_cnt.append([check_count, poet['cat_paragraphs'].iloc[i] ,poet['author'].iloc[i], poet['title'].iloc[i], poet['tags'].iloc[i]])

           

    #sort 
    sorted(rst_cnt, key=lambda x: x[0], reverse=True)

    print("=="*7+"result author"+"=="*7)
    for i in rst_atr:
        print(i)

    print("=="*7+"result title"+"=="*7)
    for i in rst_tit:
        print(i)

    print("=="*7+"result content"+"=="*7)
    for i in rst_cnt:
        if i[0] < min_count:
            break
        print(i)

    rst = [rst_cnt, rst_atr, rst_tit]
    return rst
    



