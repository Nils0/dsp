# The football.csv file contains the results from the English Premier League. 
# The columns labeled Goals and Goals Allowed contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in for and against goals.


import csv

min=1000
clubmax = ""

with open('football.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		if row[5] != "Goals":
			if abs(int(row[6]) - int(row [5])) < min:
				min = abs(int(row[6]) - int(row [5]))
				clubmax = row[0]

print clubmax, " is the club with the smallest difference. The difference is", min,"."
	#return
