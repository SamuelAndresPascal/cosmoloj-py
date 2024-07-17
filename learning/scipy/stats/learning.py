from scipy import stats

lbda=4
result = stats.expon.pdf(0.2, loc=1, scale=1/lbda)
print(result)
result = stats.expon.cdf(0.2, loc=1, scale=1/lbda)
print(result)
result = stats.expon.ppf(0.2, loc=1, scale=1/lbda)
print(result)

result = stats.gamma.pdf(0.2, a=1, loc=1, scale=1/lbda)
print(result)
result = stats.gamma.cdf(0.2, a=1, loc=1, scale=1/lbda)
print(result)
result = stats.gamma.ppf(0.2, a=1, loc=1, scale=1/lbda)
print(result)

mean=1
sd=0.25
result = stats.norm.pdf(0.2, loc=mean, scale=sd)
print(result)
result = stats.norm.cdf(0.2, loc=mean, scale=sd)
print(result)
result = stats.norm.ppf(0.2, loc=mean, scale=sd)
print(result)
