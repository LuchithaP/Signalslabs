import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-32, 32, 1)
fig, axes = plt.subplots(4,1, sharey='all', figsize=(18,18))

A = 1
w0 = 2*np.pi/12
xn1 = A*np.cos(w0*n)
w0 = 2*np.pi/6
xn2 = A*np.cos(w0*n)
w0 = 8*np.pi/31
xn3 = A*np.cos(w0*n)
w0 = 1/1.5
xn4 = A*np.cos(w0*n)

axes[0].stem(n,xn1)
axes[0].set_xlabel('$n$')
axes[0].set_ylabel('$cos(2*pi/12*n)$')
axes[0].grid(True)

axes[1].stem(n,xn2)
axes[1].set_xlabel('$n$')
axes[1].set_ylabel('$cos(2*pi/6*n)$')
axes[1].grid(True)

axes[2].stem(n,xn3)
axes[2].set_xlabel('$n$')
axes[2].set_ylabel('$cos(8*pi/31*n)$')
axes[2].grid(True)

axes[3].stem(n,xn4)
axes[3].set_xlabel('$n$')
axes[3].set_ylabel('$cos(1/1.15*n)$')
axes[3].grid(True)

plt.show()
