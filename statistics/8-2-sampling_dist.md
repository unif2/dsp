[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

import random

import numpy as np

import thinkstats2

import math

import thinkplot

import matplotlib.pyplot as plt

def RMSE(estimates, actual):

	e2 = [(estimate - actual)**2 for estimate in estimates]

	mse = np.mean(e2)

	return math.sqrt(mse)

def estimate(n, m=1000):

	lam = 2

	means = []

	for i in range(m):

		xs = np.random.exponential(1.0/lam, n)

		L = 1/np.mean(xs)

		means.append(L)

	cdf = thinkstats2.Cdf(means)

	ci = cdf.Percentile(5), cdf.Percentile(95)

	stderr = RMSE(means, 2)

	return cdf, ci, stderr

cdf1, ci1, stderr1 = estimate(10)

print("Standard error: ", stderr1)

print("90% Confidence Interval: ", ci1)

thinkplot.Cdfs([cdf1])

thinkplot.show(xlabel='L estimate with sample size 10', ylabel='CDF')

se = []

n_vals = [10, 100, 1000, 10000]

for n in n_vals:

	cdf, ci, stderr = estimate(n)

	se.append(stderr)

plt.scatter(n_vals, se)

plt.xlabel('n')

plt.ylabel('Standard Error')

plt.savefig('exercise8_stderr_plot.png')

![alt text](https://github.com/unif2/dsp/blob/master/exercise8_cdf.png "Sampling Distribution for L")
![alt text](https://github.com/unif2/dsp/blob/master/exercise8_stderr_plot.png "Standard Error versus n")
	

