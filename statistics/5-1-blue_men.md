[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

5.19466692577 percent of the US male poluation is in the right range for the Blue Man Group.

Code:


import nsfg
import thinkplot
import thinkstats2
import math
import scipy.stats

inchincm = 2.54		# not sure if this is the right value
feetincm = 33		# not sure if this is the right value

lowrange = 5 * feetincm + 10 * inchincm
highrange = 6 * feetincm + 1 * inchincm

share = (scipy.stats.norm.cdf(highrange, loc=178, scale=7.7) - scipy.stats.norm.cdf(lowrange, loc=178, scale=7.7))*100

print share, "percent of the US male poluation is in the right range for the Blue Man Group."
