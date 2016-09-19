[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

The distribution seems to be uniform. This can be best seen when looking at the CDF which is a straight line. The PMF looks rather messy in comparison and it is harder to see that the distribution is uniform.

Python code:


import nsfg
import thinkplot
import thinkstats2
import math
import random

i = 0
d = list()

while i < 1000:
	d.append(random.uniform(0,1))
	i +=1

#hist = thinkstats2.Hist(d)
#print hist

#thinkplot.Hist(hist)
#thinkplot.Show(xlable = 'value', ylable = 'Probability')

pmf = thinkstats2.Pmf(d)
#print pmf

thinkplot.Pmf(pmf)
thinkplot.Show(xlable = 'value', ylable = 'Probability')

cdf = thinkstats2.Cdf(d)

thinkplot.Cdf(cdf)
thinkplot.Show(xlable = 'value', ylable = 'Percentile')

