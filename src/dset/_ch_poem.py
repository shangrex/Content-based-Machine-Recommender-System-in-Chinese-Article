from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
from collections import Counter
from torch.utils.data import Dataset
import torch 
import numpy as np
import pysnooper
from torch.nn.utils.rnn import pad_sequence
from src.dset.util import trim_sequence


class chpoemdset(Dataset):
	def __init__(self, mode, tokenizer, num_limit_author):
		#read data
		self.data = pd.read_csv('data/poet.csv')
		#read stopwords
		self.stopwords = []
		fstp = open('data/stopwords/_ch_poem.txt', 'r')
		for i in fstp.read():
			self.stopwords.append(i)
		#set data's len
		self.len = len(self.data)
		#set data mode
		self.mode = mode
		self.tknzr = tokenizer
		self.c = Counter()
		self.c.update(self.data.author.values)
		self.lb2id = {}
		self.id2lb = {}
		self.author = []
		label_count = 0


		#limit the author 
		wanted_author = []
		for i, j in self.c.most_common():
			if j < num_limit_author:
				break
			wanted_author.append(i)
		filter_author = []
		for i in self.data['author']:
			if i in wanted_author:
				filter_author.append(True)
			else:
				filter_author.append(False)
	
		self.data = self.data.loc[filter_author]
		#make one hot encoding for author
		self.author = [[i] for i in wanted_author]

		self.one_hot = OneHotEncoder()
		self.one_hot.fit(self.author)
		self.train_df, self.test_df = train_test_split(self.data,train_size=0.95, test_size=0.05, random_state=1)
		# self.train_df = self.data

	# @pysnooper.snoop()
	def __getitem__(self, idx: int):
		if self.mode == "test":
			txt = self.test_df['paragraphs'].iloc[idx]
			# print(self.test_df['author'].iloc[idx])
			lbl = self.one_hot.transform([[self.test_df['author'].iloc[idx]]])
			# lal = None
		elif self.mode == "train":
			txt = self.train_df['paragraphs'].iloc[idx]
			# print(txt)
			# print(self.train_df['author'].iloc[idx])
			lbl = self.one_hot.transform([[self.train_df['author'].iloc[idx]]])
		else:
			txt = self.data['paragraphs'].iloc[idx]
			lbl = self.one_hot.transform([[self.data['author'].iloc[idx]]])

		seq_enc = ['[CLS]']
		txt = self.tknzr.tokenize(txt)
		seq_enc += txt
		seq_enc = [i for i in seq_enc if i not in self.stopwords]


		seq_enc = self.tknzr.convert_tokens_to_ids(seq_enc)
		# print(seq_enc)
		# print(lbl.toarray())
		return (torch.tensor(seq_enc), torch.tensor(lbl.toarray()[0]))


	def __len__(self):
		if self.mode == "train":
			return len(self.train_df)
		elif self.mode == "test":
			return len(self.test_df)
		else:
			return len(self.data)

	def dtknz(self, tkz):
		return self.tknzr.convert_ids_to_tokens(tkz)

	def dauthor(self, author):
		author = np.array(author)
		return self.one_hot.inverse_transform([author])[0]

	def len_lbl(self):
		return len(self.author)

	def create_mini_batch(self, samples):
		token_tensor = [s[0] for s in samples]
		lbl_tensor = torch.stack([s[1] for s in samples])
		token_tensor = pad_sequence(token_tensor, batch_first=True)
		token_tensor = trim_sequence(token_tensor, 200)
		# print("label tensor")
		# print(lbl_tensor)
		# print(type(lbl_tensor))
		# print("token tensor")
		# print(token_tensor)
		# print(type(token_tensor))


		mask_tensor = torch.zeros(token_tensor.shape, dtype=torch.long)
		mask_tensor = mask_tensor.masked_fill(token_tensor != 0, 1)
		return (token_tensor, mask_tensor, lbl_tensor)

	def check_author(self):
		return [i[0] for i in self.author]

		




