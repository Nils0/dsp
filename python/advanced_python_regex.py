import csv


# question 1

degrees = dict()

with open('faculty.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		degree = row[1]
		degree = degree.replace(".","")
		if degree[0]==" ":
			degree = degree[1:]
		if degree != '0' and degree != 'degree':
			if degree not in degrees:
				degrees[degree] = 1
			else:
				degrees[degree] += 1

print "Question 1: There are ", len(degrees), " different degrees. The frequencies and names are as follows: ", degrees


# question 2

titles = dict()
 
with open('faculty.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		title = row[2]
		title = title.replace(".","")
		title = title.replace(" is ", " of ")
		if title[0]==" ":
			title = title[1:]
		if title != 'title':
			if title not in titles:
				titles[title] = 1
			else:
				titles[title] += 1

print "Question2: There are ", len(titles), " different titles. The frequencies and names are as follows: ", titles


# question 3

emails = list()

with open('faculty.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		email = row[3]
		if email[0]==" ":
			email = email [1:]
		if email != 'email':
			emails.append(email)

print "Question3: There are", len(emails), "email adresses. They are as follows", emails

# question 4

domains = list()

for email in emails:
	i = email.index('@')
	domain = email[i+1:]
	if domain not in domains:
		domains.append(domain)

print "Question4: There are", len(domains), " uniquie domains. The list of unique domains is:", domains







