'''
the script is to return similar author from the selected poet
'''
from torch.utils.data import DataLoader
from tqdm import tqdm
from transformers import *
from torch.utils.tensorboard import SummaryWriter
from sklearn.metrics.pairwise import cosine_similarity
from src.dset.util import trim_sequence
import tensorflow as tf
import os
import argparse
import torch 

# from src.dset import chpoemdset
from src.dset._ch_poem import chpoemdset 

def poet_atr(txt = "白日依山"):

    model_name = "data/pretrain/5/"
    limit_number = 252
    
    topk = 15

    print("input txt: ", txt)

    tokenizer =  AutoTokenizer.from_pretrained('bert-base-chinese')

    model = AutoModelForSequenceClassification.from_pretrained(model_name)


    poem_dset = chpoemdset("all", tokenizer, limit_number)

    #input transfer to inoput tensor
    seq_enc = ['[CLS]']
    txt = tokenizer.tokenize(txt)
    seq_enc += txt
    seq_enc = tokenizer.convert_tokens_to_ids(seq_enc)
    # input_tensor = trim_sequence(seq_enc, 200)
    input_tensor = torch.tensor(seq_enc)
    mask_tensor = torch.zeros(input_tensor.shape, dtype=torch.long)
    mask_tensor = mask_tensor.masked_fill(input_tensor != 0, 1)

    model.eval()

    outputs = model(input_ids = input_tensor.unsqueeze(dim=0),
                    attention_mask = mask_tensor.unsqueeze(dim=0))


    logits = outputs[0]
    predict_values, predict_indexes = torch.topk(logits.data, topk)
    predict_indexes = predict_indexes[0]


    rst = []
    for k in range(topk):
        index = predict_indexes[k].item()
        print("predict index", index)
        predict_author = torch.zeros(300)
        predict_author[index] = 1
        print("predict author", poem_dset.dauthor(predict_author))
        rst.append(poem_dset.dauthor(predict_author))
    
    return rst


                