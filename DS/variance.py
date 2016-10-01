import numpy as np
import matplotlib.pyplot as plt

income = np.random.normal(100.0 , 20.0 , 10000)
plt.hist(income,50)
plt.show()