import numpy as np
import matplotlib.pyplot as plt
fs = 4.4e4 # sampling frequency(4.4*10^4)
ts = 1/fs
t = np.arange(-1., 1., ts)
C = 1
a  = 1.2

xt = C*np.exp(a*t)
xt1 = t + 1
fig , ax = plt.subplots()
ax.plot(t,xt,label = '$e^(at)$')
ax.set_xlabel('time')
ax.set_ylabel('sigal')
plt.legend(loc='lower right')
ax.grid(True)
plt.show()