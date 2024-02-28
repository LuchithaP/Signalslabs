import numpy as np
import matplotlib.pyplot as plt

def x(t):
  if t < 0:
    return 0 
  elif t < 1. : 
    return 1.
  elif t < 2.:
    return 2. - t
  else:
    return 0.
  
fs = 4.4e4
ts = 1 / fs 
t = np.arange(-3.5,3.5,ts)
fig , axes = plt.subplots(7,1,sharey='all',figsize=(10,15))

axes[0].plot(t,[x(t_) for t_ in t])
axes[0].set_xlabel('$t$')
axes[0].set_ylabel('$x(t)$')
axes[0].grid(True)

axes[1].plot(t,[x(t_-1) for t_ in t])
axes[1].set_xlabel('$t$')
axes[1].set_ylabel('$x(t-1)$')
axes[1].grid(True)

axes[2].plot(t,[x(t_+1) for t_ in t])
axes[2].set_xlabel('$t$')
axes[2].set_ylabel('$x(t+1)$')
axes[2].grid(True)

axes[3].plot(t,[x(t_*(-1)) for t_ in t])
axes[3].set_xlabel('$t$')
axes[3].set_ylabel('$x(-t)$')
axes[3].grid(True)

axes[4].plot(t,[x(t_*(-1)+1) for t_ in t])
axes[4].set_xlabel('$t$')
axes[4].set_ylabel('$x(-t+1)$')
axes[4].grid(True)

axes[5].plot(t,[x(3*t_/2) for t_ in t])
axes[5].set_xlabel('$t$')
axes[5].set_ylabel('$x(3t/2)$')
axes[5].grid(True)

axes[6].plot(t,[x(3*t_/2+1) for t_ in t])
axes[6].set_xlabel('$t$')
axes[6].set_ylabel('$x(3t/2+1)$')
axes[6].grid(True)

plt.show()
