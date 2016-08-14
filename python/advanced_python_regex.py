Q1

import string
import csv


file = open('faculty.csv')
reader = csv.reader(file)
data = list(reader)
data[0]=[word.strip(' ') for word in data[0]]
	
deg_index = data[0].index('degree')
degrees = []
for i in range(1,len(data)):
	degree = data[i][deg_index]
	degree.split()
	degree = degree.strip(string.punctuation + string.whitespace)
	degree = degree.lower()
	degrees.append(degree)
newlist = []
for word in degrees:
	if ' ' in word:
		newlist.extend(word.split())
	else:
		newlist.append(word)
newlist2=[]
for word in newlist:
	word=word.lower()
	newlist2.append(word.replace('.',''))

hist = dict()	
for word in newlist2:
	hist[word]=hist.get(word,0)+1

print(hist)
# Returns {'jd': 1, 'ma': 1, '0': 1, 'md': 1, 'phd': 31, 'scd': 6, 'mph': 2, 'bsed': 1, 'ms': 2}
# Therefore, there are 8 different degrees, one person didn't have any degrees.  By far, the most frequent degree
# is the PhD

Q2

