import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors

#Part A
df=pd.read_csv("star_cluster (1).csv")

#Part B
df_new = df.drop(df[(abs(df['x']) >= 20 ) & (abs(df['y']) >= 20) & (abs(df['z']) >= 20)].index)

#Part C
vx=df_new['vx']
vy=df_new['vy']
plt.hist2d(vx,vy,bins=100,norm=colors.LogNorm())
cbar = plt.colorbar()

#Part D
df_massive=df.drop(df[(df['mass'] > 1)].index)
df_light=df.drop(df[(df['mass'] <= 1)].index)

#Part E
ax = plt.axes(projection='3d')
x=df_massive['x']
y=df_massive['y']
z=df_massive['z']


x1=df_light['x']
y1=df_light['y']
z1=df_light['z']

ax.scatter3D(x, y, z, color = "green")
ax.scatter3D(x1, y1, z1, color = "blue")

plt.xlim(0, 20)
plt.ylim(0, 20)

plt.show()