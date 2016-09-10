import csv


# question 6


faculty_dict = {}

second_namesl = list()

with open('faculty.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		if row[0] != "name":
			i = row[0].rindex(" ")
			name = row[0][i+1:]
			info = [row[1], row[2], row[3]]
			if name not in second_namesl:
				faculty_dict[name]=info
			else:
				faculty_dict[name]=[faculty_dict[name], info]
			second_namesl.append(name)

print "Question 6: "
j=0
for i in faculty_dict:
	if j<=2:
		print i, ":", faculty_dict[i]
		j += 1


# question 7

professor_dict = {}

with open('faculty.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		if row[0] != "name":
			i = row[0].rindex(" ")
			j = row[0].index(" ")
			second_name = row[0][i+1:]
			first_name = row[0][:j]
			name = (first_name, second_name)
			info = [row[1], row[2], row[3]]
			professor_dict[name]=info


print "Question 7:"			
j=0
it = iter(sorted(professor_dict.iteritems()))
while j<=2:
	print it.next()
	j += 1


# question 8

keylist = sorted(professor_dict)
keylist = sorted(keylist, key = lambda x: x[1])

print "Question 8:"
j=0
while j<=2:
	print keylist[j], " : ", professor_dict[keylist[j]]
	j+=1




# print it.next()


