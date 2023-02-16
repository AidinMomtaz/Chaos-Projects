import random as rn
import numpy as np
import matplotlib.pyplot as plt

M=[]
Pm=[]
rn.seed(190909)
const=-0.3/((100**-0.3)-(0.1**-0.3))
for i in range(100000):
    f=rn.random()
    
    m=(((100**-0.3)-(0.1**-0.3))*f+(0.1**-0.3))**(-1/0.3)
    pm=const*m**-1.3
    M.append(m)
    Pm.append(pm)
    
M=np.array(M)    
a=np.log10(min(Pm))
b=np.log10(max(Pm))
mybins=np.logspace(a,b,num=10)
    
plt.hist(Pm, bins=mybins, density='True',histtype='step',log=True)


plt.xlabel("M")
plt.ylabel("PDF")
#Fit

xavg=np.mean(M)
yavg=np.mean(Pm)
Surat=0
Makhraj=0
for j in range(100000):
    Surat+=(Pm[j]*(Pm[j]-xavg))
    Makhraj+=(M[j]*(M[j]-xavg))
B=Surat/Makhraj
A=yavg-xavg*B 
y=A+B*M   

plt.scatter(M, y)
plt.xscale("log")
plt.yscale("log")
plt.tight_layout()
plt.show()
   