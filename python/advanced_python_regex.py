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

title_index = data[0].index('title')
titles = []
for i in range(1,len(data)):
	title = data[i][title_index]
	title = title.lower()
	if 'associate' in title:
		titles.append('associate')
	elif 'assistant' in title:
		titles.append('assistant')
	else:
		titles.append('full')

d = dict()
# Code for making a dictionary of titles with counts, but of course
# we can just use the get(word,0) + 1 like above, but let's do it this
# way
for x in titles:
	if x not in d:
		d[x] = 1
	else:
		d[x]+=1
		
print(d)
# Returns {'assistant': 12, 'associate': 12, 'full': 13}

Q3

email_index = data[0].index('email')

emails = []

for i in range(1,len(data)):
	emails.append(data[i][email_index])
print(emails)

# Returns ['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', 'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'pgimotty@upenn.edu', 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu', 'whwang@mail.med.upenn.edu', 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu', 'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu', 'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu', 'michross@upenn.edu', 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu', 'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu', 'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu', 'weiyang@mail.med.upenn.edu']

Q4

domains = {}
for i in range(1,len(data)):
	p = data[i][email_index].index('@')
	domain = data[i][email_index][p+1:]
	domains[domain]=domains.get(domain,0)+1

print(domains)
print(len(domains))

# Returns {'upenn.edu': 12, 'mail.med.upenn.edu': 23, 'cceb.med.upenn.edu': 1, 'email.chop.edu': 1}
# Returns 4.  There are 4 different email domains
