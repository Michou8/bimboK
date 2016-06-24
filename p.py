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
		word = line[1]
		data[line[0]] = 0
		#for word in pr.split():
		#word = word.lower()
		match = re.search('[0-9]+(g|ml|kg)',word.lower())
		matchp = re.search('[0-9]+p',word.lower())
		p = -1
		if matchp:
			p= int(matchp.group().replace('p',''))
			if p ==0:
				p = 1
				
		weight = -1
		if match:
			if 'kg' in match.group():
				weight = int(match.group().replace('ml','').replace('kg',''))*1000
			else:
				if 'ml' in match.group() or 'g' in match.group():
	        			weight = int(match.group().replace('ml','').replace('g',''))
		if p<0 and weight <0:
			data[line[0]] = -weight*p
		else:
			data[line[0]] = weight*p
		
		print data[line[0]]
		print line

with open('vocab.json','wb') as f:
	json.dump(vocab,f,indent=2)
vocab_w_int = {}
from nltk.corpus import stopwords
stop = stopwords.words("spanish")
for key in vocab:

	try:
		int(key)
	except:
		match = re.search('[0-9]+(g|ml|kg)',key.lower())
		matchp = re.search('[0-9]+p',key.lower())
		if key not in stop:
			vocab_w_int[key] = vocab[key]
with open('vocab_w_int.json','wb') as f:
        json.dump(vocab_w_int,f,indent=2)
