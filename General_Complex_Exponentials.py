import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-12, 12, 1)
fig, axes = plt.subplots(2,1,sharex='all',sharey='all',figsize = (18,18))
theta = 0.0
C = 1
alpha = 1.1
w0 = 2*np.pi/12

ReXn1 = (abs(C)*(abs(alpha))**n)*np.cos(w0*n + theta)

alpha = 0.92

ReXn2  = (abs(C)*(abs(alpha))**n)*np.cos(w0*n + theta)

axes[0].plot(n,ReXn1)
axes[0].set_xlabel('$n$')
axes[0].set_ylabel('$alpha=1.1$')
axes[0].grid(True)

axes[1].plot(n,ReXn2)
axes[1].set_xlabel('$n$')
axes[1].set_ylabel('$alpha=0.92$')
axes[1].grid(True)

plt.show()