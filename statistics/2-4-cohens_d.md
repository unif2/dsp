[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> 
import thinkstats2

import nsfg

import numpy as np

import thinkplot

import first

preg = nsfg.ReadFemPreg()

live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]

others = live[live.birthord != 1]

hist1 = thinkstats2.Hist(firsts.totalwgt_lb)

hist2 = thinkstats2.Hist(others.totalwgt_lb)

width = 0.45

thinkplot.PrePlot(2)

thinkplot.Hist(hist1, width=width)

thinkplot.Hist(hist2, width=width)

thinkplot.Show(xlabel='weight', ylabel='frequency')

mean0 = live.totalwgt_lb.mean()

mean_firsts = firsts.totalwgt_lb.mean()

var_firsts = firsts.totalwgt_lb.var()

mean_others = others.totalwgt_lb.mean()

var_others = others.totalwgt_lb.var()

diff = mean_firsts - mean_others

n1, n2 = len(firsts.totalwgt_lb), len(others.totalwgt_lb)

pooled_var = (n1*var_firsts + n2*var_others)/(n1+n2)

Cohen_d = diff/np.sqrt(pooled_var)

print("Difference in mean birth weight between first babies and others: ", diff, "Cohen's d: ", Cohen_d)

print("Mean birthweight for all births: " , mean0)

# Result: difference in means = -0.125 lbs, Cohen's d = -0.089

# It seems like first babies are lighter.  Difference in means is about 0.089 standard deviations

m0 = live.prglngth.mean()

m1 = firsts.prglngth.mean()

m2 = others.prglngth.mean()

v1 = firsts.prglngth.var()

v2=others.prglngth.var()

diff2 = m1-m2

pooled2 = (n1*v1+n2*v2)/(n1+n2)

Cohen_d2 = diff2/np.sqrt(pooled2)

print("Difference in mean pregnancy length between first babies and others: ", diff2, "Cohen's d: ", Cohen_d2)

print("Mean pregnancy length for all completed pregnancies: ", m0)

# Result: difference in means = 0.078 weeks, Cohen's d = 0.029

# It seems like first babies take longer.  Difference in means is about 0.029 standard deviations

# It seems like the effect is three times less for pregnancy length than birth weight

![alt text](https://github.com/unif2/dsp/blob/master/exercise1.png "Histograms for first babies and others")
