import numpy as np
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
import time

comandos = ['saudacoes', 'alo alo peixe', 'eueu eu']

com = 'peixe bola gato mister flamengo gabigol'
test = 'oi'

n = 1

counts = CountVectorizer(analyzer='word', ngram_range=(n,n))

vocab2int = counts.fit([com, test]).vocabulary_

n_grams = counts.fit_transform([com, test])

intersection_list = np.amin(n_grams.toarray(), axis = 0)

intersection_count = np.sum(intersection_list)

print(intersection_count)

