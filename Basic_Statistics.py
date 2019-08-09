#Gaurav More
#PRN: 10303320181124510065

import numpy as np

from scipy import stats

n = int(input())
x = [int(i) for i in input().split()]

mean = np.mean(x)
median = np.median(x)
mode = stats.mode(x).mode[0]

sd = np.std(x)
ld = mean - ( 1.96 * sd / np.sqrt(n))
ud = mean + ( 1.96 * sd / np.sqrt(n))

print(mean)
print(median)
print(mode)
print('{0:.1f}'.format(sd))
print('{0:.1f}'.format(ld), '{0:.1f}'.format(ud))
