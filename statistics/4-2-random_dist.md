[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> import chap01soln
import thinkstats2
import thinkplot

resp = chap01soln.ReadFemResp()

pmf_actual = thinkstats2.Pmf(resp.numkdhh)

pmf_bias = pmf_actual.Copy(label='biased')

for x, p in pmf_actual.Items():
	pmf_bias.Mult(x,x)

pmf_bias.Normalize()

def mean_from_pmf(pmf):
	mean = 0
	for x, p in pmf.Items():
		mean += x*p
	return mean

mean_actual = mean_from_pmf(pmf_actual)
mean_bias = mean_from_pmf(pmf_bias)

print("Actual mean: ", mean_actual)
print("Biased mean: ", mean_bias)

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf_actual, pmf_bias])
thinkplot.Show(xlabel='Number of children under 18', ylabel='PMF')

# As expected the mean of the biased distribution is higher.
# Also, as expected, the biased PMF shows no instances of households with no children
# under 18.
