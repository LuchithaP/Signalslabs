import numpy as np
import matplotlib.pylab as plt

fs = 44100 # 44,100−Hz sampling frequency
ts = 1/fs
t = np.arange(-1, 1, ts) # A linearly−spaced array with step ts
f = 2 # 2 Hz
A = 1
w0 = 2*np.pi
phi = np.pi/2
fig, axes = plt.subplots(2 ,2 , sharex='all', sharey='all', figsize=(18,18))
# Your code goes here
xt1 = A*np.cos(w0*t)
xt2 = (A/2)*np.cos(w0*t)
xt3 = -A*np.sin(w0*t)
xt4 = A*np.cos(2*w0*t)

# Your code goes here

axes[0, 0].plot(t,xt1)
axes[0, 0].set_xlabel('time')
axes[0, 0].set_ylabel('signal')
axes[0, 0].grid(True)
axes[0, 0].title.set_text(' $\cos(2\pi t)$')

axes[0, 1].plot(t,xt2)
axes[0, 1].set_xlabel('time')
axes[0, 1].set_ylabel('signal')
axes[0, 1].grid(True)
axes[0, 1].title.set_text('$0.5\cos(2\pi t)$')


axes[1, 0].plot(t,xt3)
axes[1, 0].set_xlabel('time')
axes[1, 0].set_ylabel('signal')
axes[1, 0].grid(True)
axes[1,0].title.set_text('$-\sin(2\pi t)$')


axes[1, 1].plot(t,xt4)
axes[1, 1].set_xlabel('time')
axes[1, 1].set_ylabel('signal')
axes[1, 1].grid(True)
axes[1, 1].title.set_text('$\cos(4\pi t)$')
plt.show()



