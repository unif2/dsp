# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
file = open('football.csv')
reader = csv.reader(file)
data = list(reader)
g_index = data[0].index('Goals')
ga_index = data[0].index('Goals Allowed')

diff = []
diff.append(None)
for i in range(1,len(data)):
  diff.append(int(data[i][g_index]) - int(data[i][ga_index]))
print(data[diff.index(min(diff[1:]))][0])
