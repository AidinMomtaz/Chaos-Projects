import numpy as np
from matplotlib import pyplot as plt
from scipy import random
#A

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def f(x):
   return np.sin(x)*(1-x)**2

x = np.arange(0,np.pi,0.01)

plt.plot(x, f(x), color='red')

plt.show()

#B


a = 0
b = np.pi
Nlist=[int(1e3),int(1e4),int(1e5),int(1e6)]
anslist=[]
for j in Nlist:
    
    # array of zeros of length N
    ar = np.zeros(j)
    
    # iterating over each Value of ar and filling
    # it with a random value between the limits a
    # and b
    for i in range(len(ar)):
    	ar[i] = random.uniform(a, b)
    
    # variable to store sum of the functions of
    # different values of x
    integral = 0.0
    
    
    
    # iterates and sums up values of different
    # functions of x
    for i in ar:
    	integral += f(i)
    
    # we get the answer by the formula derived adobe
    ans = (b-a)/float(j)*integral
    anslist.append(ans)
    # prints the solution
    #print("The value calculated by monte carlo integration is {}.".format(ans))
plt.scatter(Nlist, anslist, color='green')