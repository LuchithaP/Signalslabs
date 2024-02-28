import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline


fs  = 44100
ts = 1/fs
t = np.arange(-1,1,ts)
A = 1
f = 2
w0 = 2*np.pi*f
phi  = 0
xt = A*np.cos(w0*t+phi)
fig,ax = plt.subplots()
ax.plot(t,xt)
plt.show()