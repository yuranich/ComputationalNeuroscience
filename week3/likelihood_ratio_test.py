import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = norm.stats(moments='mvsk')

x = np.linspace(4, 9, 100)
ax.plot(x, 2 * norm.pdf(x, loc = 5, scale = 0.5), 'r-', lw=5, alpha=0.6, label='first pdf')
ax.plot(x, norm.pdf(x, loc = 7, scale = 1), 'b-', lw=5, alpha=0.6, label='second pdf')
plt.show()