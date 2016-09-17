[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---

import random
import numpy as np
import math
import thinkstats2
import thinkplot
import matplotlib.pyplot as plt

def game(lam):
	times = []
	sum = 0
	while sum < 1:
		x = random.expovariate(lam)
		sum += x
		if sum > 1:
			break
		else:
			times.append(x)
		
	return len(times)

def simulation(lam, m):
	estimates = [game(lam) for _ in range(m)]
	e1 = [estimate - lam for estimate in estimates]
	e2 = [(estimate - lam)**2 for estimate in estimates]
	mse = np.mean(e2)
	rmse = math.sqrt(mse)
	me = np.mean(e1)
	cdf = thinkstats2.Cdf(estimates)
	ci = cdf.Percentile(5), cdf.Percentile(95)
	return me, rmse, ci, cdf, estimates

me, rmse, ci, cdf, estimates = simulation(5, 10000)

print("Standard error: ", rmse)  # 2.22
print("90% Confidence Interval: ", ci)  # (2,9)

thinkplot.Cdfs([cdf])
thinkplot.show(xlabel="Lambda Estimate with actual value 5", ylabel="CDF")

print(np.mean(estimates))  # 5.02

lam_vals = [3, 6, 9, 12, 15, 18, 21]
errors = []

for lam in lam_vals:
	me, rmse, ci, cdf, estimates = simulation(lam, 10000)
	errors.append(rmse)

print(errors) # They are increasing.

---
