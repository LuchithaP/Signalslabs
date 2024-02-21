import numpy as np
import matplotlib.pyplot as plt
fs = 4.4e4 # sampling frequency(4.4*10^4)
ts = 1/fs
t = np.arange(-1., 1., ts)
f = 5
w0 = 2*np.pi*f
C = 0.15
phi1,phi2 = 0 , np.pi/2
r =2
xt1 = C*np.exp(r*t)*np.cos(w0*t + phi1)
xt2 = C*np.exp(-r*t)*np.cos(w0*t + phi2)

fig, axes = plt.subplots(1 ,2 , sharex='all', sharey='all', figsize=(12,12))

axes[0].plot(t,xt1)
axes[0].set_xlabel('time')
axes[0].set_ylabel('signal')
axes[0].grid(True)
axes[0].title.set_text('$e^rcos(wt)$')

axes[1].plot(t,xt2)
axes[1].set_xlabel('time')
axes[1].set_ylabel('signal')
axes[1].grid(True)
axes[1].title.set_text('$e^rcos(wt+ pi/2)$')

plt.show()