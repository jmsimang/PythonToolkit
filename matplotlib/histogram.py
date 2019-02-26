import matplotlib.pyplot as plt
import numpy as np

values = np.random.randn(50) + 6
plt.hist(values, bins=5)
plt.show()
plt.savefig('histogram.png')
plt.clf()
