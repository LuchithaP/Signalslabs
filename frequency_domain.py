import numpy as np
import matplotlib.pyplot as plt

fs = 100# 100−Hz sampling frequency
ts = 1/fs
t = np.arange(-1., 1., ts) # A linearly−spaced array with step ts
fig, axes = plt.subplots(2,1, figsize=(10,10))
f = 2 # 2 Hz
omega0 = 2*np.pi*f
xt = 0.75 + 2.*np.cos(omega0*t) + 1.*np.cos(3*omega0*t)
Xf = np.fft.fft(xt)
freq = np.fft.fftfreq(t.shape[-1], d=ts)
axes[0].plot(t,xt)
axes[0].set_xlabel('$t$ in s')
axes[0].set_ylabel('$x(t)$')
valsubrange = np.concatenate((np.arange(0,21,1), np.arange(-1,-21,-1)))
freqsubrage = np.concatenate((np.arange(0,21,1), np.arange(-1,-21,-1)))
axes[1].stem(freq[freqsubrage], Xf.real[valsubrange]/len(t))
axes[1].set_xlabel('$f$ in Hz')
axes[1].set_ylabel('$\mathfrak{Re}(X(j\omega))$')
plt.xticks(np.arange(-10,11))
plt.show()

