import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 10., 1)

fig, axes = plt.subplots(2,2, sharex='all', sharey='all', figsize=(18,18))
C = 1.0
alpha = 1.1
xn1 = C*alpha**(n)
alpha = 0.92
xn2 = C*alpha**(n)
alpha = -1.1
xn3 = C*alpha**(n)
alpha = -0.92
xn4 = C*alpha**(n)


axes[0, 0].stem(n,xn1) # stem is used for discrete function plotting
axes[0, 0].set_xlabel('$n$')
axes[0, 0].set_ylabel('$1.1^{n}$')
axes[0, 0].grid(True)

axes[0, 1].stem(n,xn2)
axes[0, 1].set_xlabel('$n$')
axes[0, 1].set_ylabel('$0.92^{n}$')
axes[0, 1].grid(True)

axes[1, 0].stem(n,xn3)
axes[1, 0].set_xlabel('$n$')
axes[1, 0].set_ylabel('$-1.1^{n}$')
axes[1, 0].grid(True)

axes[1, 1].stem(n,xn4)
axes[1, 1].set_xlabel('$n$')
axes[1, 1].set_ylabel('$-0.92^{n}$')
axes[1, 1].grid(True)



plt.show()