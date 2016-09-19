[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Answer: First babies are in the mean 0.124761184535 lb lighter than 'other' babies. Cohen's d is: -0.0571520474781 . Hence, the difference is  -0.0571520474781  standard deviations which is approx. twice as much as for the pregnancy length.


Python Code:

import nsfg
import thinkplot
import thinkstats2
import math

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

#print firsts.totalwgt_lb.mean()

diff = firsts.totalwgt_lb.mean() - others.totalwgt_lb.mean()

var1 = firsts.totalwgt_lb.var()
var2 = others.totalwgt_lb.mean()

n1 = len(firsts)
n2 = len(others)

pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)

d = diff / math.sqrt(pooled_var)

print "First babies are in the mean", -diff, "lb lighter than 'other' babies. Cohen's d is:", d, ". Hence, the difference is ", d, " standard deviations which is approx. twice as much as for the pregnancy length."

