import numpy as np
from matplotlib import pyplot as plt
from scipy import random
import math

def f(x):
   return np.sin(x**2)*math.exp(-x**0.5)
a=0
b=17
y = np.arange(a,b,1)
N=int(1e5)
#Part A
h=(b-a)/N
I=0
for k in range(1,9999):
    I+=h*(0.5*f(a)+0.5*f(b)+0.5*(f(a+k*h)))
    
#Part B

ar = np.zeros(N)

for i in range(len(ar)):
	ar[i] = random.uniform(a, b)


integral = 0.0
for i in ar:
    	integral += f(i)
ans = ((b-a)/N)*integral
      
        