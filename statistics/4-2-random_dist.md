[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> 
import random

import thinkstats2

import thinkplot

list = []

for n in range(1000):

	x = random.random()

	list.append(x)

cdf = thinkstats2.Cdf(list, label='random numbers')

thinkplot.Cdfs([cdf])

thinkplot.Show(xlabel='random number', ylabel='CDF')

![alt text](https://github.com/unif2/dsp/blob/master/exercise3_cdf.png "CDF for 1000 random numbers from random.random")

# The CDF is approximately a straight line with slope 1.  So we have a uniform distribution, since x% of the numbers
# are less than x, for any x in [0,1].

pmf = thinkstats2.Pmf(list)

thinkplot.Pmf(pmf, linewidth=0.1)

thinkplot.Show(xlabel='random number')

![alt text](https://github.com/unif2/dsp/blob/master/exercise3_pmf.png "PMF")
