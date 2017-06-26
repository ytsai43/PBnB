import numpy as np
from math import *
from random import *
delta = 0.1 #clossness parameter
alpha = 0.25 #error rate
epsilon = 0.001 #condition to terminate subregion with continuous case 
M = 2 #number of subregions
l,u=5,10 #range of variable x
middlePoint=(l + u) / 2

#objective function



#iteration
alpha = alpha / 2
N=ceil(log(alpha) / log(1-delta)) # number of sample point we need in one subregion
R=ceil(log(alpha / (2 * (M-1))) / log(0.5)) #number of replication
region1=[]
region2=[]

fHatx1=[]
hHat1=[]
fHatx2=[]
hHat2=[]
hHat=[]
mean,sigma = 0,1 
for i in range(2):
    region1.append([])
    region2.append([])
    x1=(uniform(l,middlePoint))
    x2=(uniform(middlePoint,u))
    for r in range(2): 
        noisy = np.random.normal(mean, sigma,1)
        region1[i].append(3*x1+2+noisy)
        noisy = np.random.normal(mean, sigma,1)
        region2[i].append(3*x2+2+noisy)
    region1[i].append(np.mean(region1[i])) #mean value is stored in the last position
    region2[i].append(np.mean(region2[i]))
region1.sort(key = lambda x: (x[-1]))
region2.sort(key = lambda x: (x[-1]))
comList=[region1[0][2],region2[0][2]]
rankSubregion=comList.index(min(region1[0][2],region2[0][2]))
print(region1,region2)

if rankSubregion == 0:
    del region1[0][-1]
    region1[0].sort()
    upStar=region1[0][-1]
    del region2[0][-1]
    region2[0].sort()
    downStar=region2[0][0]
    if upStar<downStar:
        del region2[:]
    
else:
    del region2[0][-1]
    region2[0].sort()
    upStar=region2[0][-1]
    del region1[0][-1]
    region1[0].sort()
    downStar=region1[0][0]
    if upStar<downStar:
        del region1[:]

print(region1, region2)





