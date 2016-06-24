import pandas as pd
import csv 
import json	
import re
data = {}
vocab = {}
with open('producto_tabla.csv') as f:
	header = f.next().strip().split(',')
	for line in f:
		line = line.strip().split(',')
		pr = line[1]
		data[line[0]] = {}
		for word in pr.split():
			word = word.lower()
			if word not in data[line[0]]:
				data[line[0]][word] = 1
				
			else:
				data[line[0]][word] += 1
			if word not in vocab:
				vocab[word] = 1
			else:
				vocab[word] += 1

with open('vocab.json','wb') as f:
	json.dump(vocab,f,indent=2)
vocab_w_int = {}
from nltk.corpus import stopwords
stop = stopwords.words("spanish")
for key in vocab:

	try:
		int(key)
	except:
		match = re.search('[0-9]+(g|ml|kg)',key)
		matchp = re.search('[0-9]+p',key)
		if matchp:
			print matchp.group()
		if key not in stop:
			vocab_w_int[key] = vocab[key]
with open('vocab_w_int.json','wb') as f:
        json.dump(vocab_w_int,f,indent=2)
