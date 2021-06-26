import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy.optimize import fsolve
inputFilePath = 'Rawdata.xlsx'
dfIn = pd.read_excel(inputFilePath)
Theta=[]
for i in range (35000):
    Theta.append(dfIn.loc[i,0])
  
min=np.min(Theta)
max=np.max(Theta)


thetaf = [((ele)*3.14)/(max)+1.57 for ele in Theta]
thetaprimef=[]
# thetaprimef = [((ele)*4*3.14)/((max))-(2*3.14) for ele in Theta]
for ele in Theta:
    if(ele>0):
       thetaprimef.append(((ele)*4*3.14)/((max))-(2*3.14))
    else:
        thetaprimef.append(((ele)*4*3.14)/((max))+(2*3.14))

dfOut = pd.DataFrame(thetaprimef)

outputFilePath = 'thetaprimef.xlsx'

dfOut.to_excel(outputFilePath, index=False)


'''plt.plot(thetaf)
plt.xlabel('Time [non-dim]')
plt.ylabel('Natural logarithm of data difference [a.u.]')
plt.title('Derivative')
plt.figure(dpi=300)
plt.show()'''