import csv

# get e-mail addresses (from part 1)


emails = list()

with open('faculty.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		email = row[3]
		if email[0]==" ":
			email = email [1:]
		if email != 'email':
			emails.append(email)


# add line breaks to the elements

delimiter2 = "\r\n-"
emails2 = delimiter2.join(emails)
emails3 = emails2.split("-")

print emails3	


with open('e-mails.csv', 'wb') as myfile:
	wr = csv.writer(myfile)
	wr.writerow(emails3)
