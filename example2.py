
import numpy as np
import matplotlib.pyplot as plt

fs = 4.4e4 # sampling frequency(4.4*10^4)
ts = 1/fs
t = np.arange(-1., 1., ts)
f = 2 # 2 Hz
w0 = 2*np.pi*f
phi = 0.
x1t = np.cos(w0*t + phi)
phi = np.pi/2
x2t = np.cos(w0*t + phi)
fig, ax = plt.subplots()
ax.plot(t,x1t, label='$\cos(4\pi t)$')
ax.plot(t,x2t, label='$\cos(4\pi t + \pi/2)$')
ax.set_xlabel('time')
ax.set_ylabel('sigal')
plt.legend(loc='lower right')
ax.grid(True)
plt.show()