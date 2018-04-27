from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
norm = norm(loc=1000, scale=150)
x = np.arange(0, 2000, 0.01)
plt.plot(x, norm.cdf(x))
plt.show()
print(1 - norm.cdf(1200))
# print(norm)
