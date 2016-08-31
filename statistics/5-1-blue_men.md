[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 
from scipy.stats import norm

min1 = 5*12*2.54 + 10*2.54

max1 = 6*12*2.54 + 1*2.54

mu = 178

sigma = 7.7

min2 = (min1 - mu)/sigma

max2 = (max1 - mu)/sigma

answer = 100*(norm.cdf(max2) - norm.cdf(min2))

print("The percentage of men who qualify is %f" %answer, "%.")

# Roughly 34.3% of the male population.
