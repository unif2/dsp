[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

import hypothesis

import thinkstats2

import numpy as np

import first

import thinkplot

class DiffMeansPermute(thinkstats2.HypothesisTest):
	
	def TestStatistic(self, data):

		group1, group2 = data

		test_stat = abs(group1.mean() - group2.mean())

		return test_stat
		
	def MakeModel(self):

		group1, group2 = self.data

		self.n, self.m = len(group1), len(group2)

		self.pool = np.hstack((group1, group2))
		
	def RunModel(self):

		np.random.shuffle(self.pool)

		data = self.pool[:self.n], self.pool[self.n:]

		return data
		
class DiffMeansResample(hypothesis.DiffMeansPermute):
	
	def RunModel(self):

		group1 = np.random.choice(self.pool, self.n, replace=True)

		group2 = np.random.choice(self.pool, self.m, replace=True)

		return group1, group2
        
live, firsts, others = first.MakeFrames()

data = firsts.prglngth.values, others.prglngth.values

ht = DiffMeansResample(data)

pvalue = ht.PValue()

ht.PlotCdf()

thinkplot.Show(xlabel='test statistic', ylabel='CDF')

![alt text](https://github.com/unif2/dsp/blob/master/exercise11_prglngth.png "CDF of difference in mean pregnancy length under the null hypothesis using Resampling")

data = firsts.totalwgt_lb.dropna().values, others.totalwgt_lb.dropna().values

ht = DiffMeansResample(data)

pvalue = ht.PValue()

ht.PlotCdf()

thinkplot.Show(xlabel='test statistic', ylabel='CDF')

![alt text](https://github.com/unif2/dsp/blob/master/exercise11_wgt.png "CDF of difference in birth weight under the null hypothesis using Resampling")
