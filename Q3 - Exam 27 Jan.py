import math
import numpy as np
import matplotlib.pyplot as plt

#Part A

#constants
C1=-4*1e-3
C2=2*1e-4
h=0.1

def dadt(t,a):
    return C1*a**2
def dedt(t,a):
    return C2*a

t = np.arange(0.0, 40.0, h)
a = np.zeros(t.size)
e = np.zeros(t.size)
a[0]=10
e[0]=0.5
for i in range(1, t.size):
    a[i] = a[i-1] + h*dadt(t[i-1] + h/2, a[i-1] + (h/2.0)*dadt(t[i-1],a[i-1]))
    e[i] = e[i-1] + h*dedt(t[i-1] + h/2, e[i-1] + (h/2.0)*dedt(t[i-1],e[i-1]))
plt.plot(t,e,'b-')
"""
def y1(t,y):
    return y
h = 0.1
t0 = 0.0
y0 = 1.0

t = np.arange(0.0, 5.0, h)
y = np.zeros(t.size)
y[0] = y0
for i in range(1, t.size):
    y[i] = y[i-1] + h*y1(t[i-1] + h/2, y[i-1] + (h/2.0)*y1(t[i-1],y[i-1]))
plt.plot(t,y,'r-')

"""