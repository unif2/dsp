[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

import nsfg

import numpy as np

import thinkplot

import thinkstats2

import math

import pandas

preg = nsfg.ReadFemPreg()

live = preg[preg.outcome == 1]

thinkplot.Scatter(live.agepreg, live.totalwgt_lb)

thinkplot.Show(xlabel='Age', ylabel='Total Birthweight')

live = live.dropna(subset=['agepreg', 'totalwgt_lb'])

bins = np.arange(10,50,5)

indices = np.digitize(live.agepreg, bins)

groups = live.groupby(indices)

ages = [group.agepreg.mean() for i, group in groups]

cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]

thinkplot.PrePlot(3)

for percent in [75, 50, 25]:

	weights = [cdf.Percentile(percent) for cdf in cdfs]

	label = '%dth' %percent

	thinkplot.Plot(ages, weights, label=label)

thinkplot.Show(xlabel='Age', ylabel='Total Birthweight')

def Cov(xs, ys, meanx=None, meany=None):

	xs = np.asarray(xs)

	ys = np.asarray(ys)
	
	if meanx is None:

		meanx = np.mean(xs)

	if meany is None:

		meany = np.mean(ys)
		

	cov = np.dot(xs - meanx, ys - meany)/len(xs)

	return cov
	

def Corr(xs, ys):

	xs = np.asarray(xs)

	ys = np.asarray(ys)
	
	meanx, varx = np.mean(xs), np.var(xs)

	meany, vary = np.mean(ys), np.var(ys)
	
	corr = Cov(xs, ys, meanx, meany)/math.sqrt(varx*vary)

	return corr

def SpearmanCorr(xs, ys):

	xs = pandas.Series(xs)

	ys = pandas.Series(ys)

	return xs.corr(ys, method='spearman')

pc = Corr(live.agepreg, live.totalwgt_lb)

print("Pearson's correlation is %r" %pc)

sc = SpearmanCorr(live.agepreg, live.totalwgt_lb)

print("Spearman's correlation is %r" %sc)

![alt text](https://github.com/unif2/dsp/blob/master/exercise7scatter.png "Scatter Plot of Birth Weight vs Age")
![alt text](https://github.com/unif2/dsp/blob/master/exercise7percentile.png "Percentiles of Birth Weight vs Age")

# Pearson's correlation is around 0.07, while Spearman's correlation is around 0.09, a bit more than Pearson's.  This 
# suggests a possible nonlinear relationship and/or the influence of outliers in the data.
# From the graph of percentiles we can see the steepest change in weight for ages between 15 and 25 and not as dramatic a 
# change past age 25.  This observation also suggests a nonlinear relationship between the two variables.
