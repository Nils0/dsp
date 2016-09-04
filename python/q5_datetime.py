# Hint:  use Google to find python function

from datetime import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

x=datetime.strptime(date_start, "%m-%d-%Y")
y=datetime.strptime(date_stop, "%m-%d-%Y")

daysbetweena = y-x   

print "The anwer to question a) is", daysbetweena

####b)  
date_start = '12312013'  
date_stop = '05282015'  

x=datetime.strptime(date_start, '%m%d%Y')
y=datetime.strptime(date_stop, '%m%d%Y')

daysbetweenb = y-x

print "The anwer to question b) is", daysbetweenb

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

x=datetime.strptime(date_start, '%d-%b-%Y')
y=datetime.strptime(date_stop, '%d-%b-%Y')

daysbetweenc = y-x

print "The anwer to question c) is", daysbetweenc
