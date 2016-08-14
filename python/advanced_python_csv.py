import string
import csv


file = open('faculty.csv')
reader = csv.reader(file)
data = list(reader)
data[0]=[word.strip(' ') for word in data[0]]

email_index = data[0].index('email')

emails = []

for i in range(1,len(data)):
	emails.append(data[i][email_index])

output_file = open('emails.csv', 'w')
wr = csv.writer(output_file)
for item in emails:
	wr.writerow([item])
