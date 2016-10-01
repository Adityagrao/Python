import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
#Mean
income = np.random.normal(27000, 15000, 10000)
print ("Showing Mean")
print (np.mean(income))

#plt.hist(income, 50)
#plt.show()

#Median

print("Showing Median")
print(np.median(income))


income = np.append(income, [1000000000])

print ("Showing Mean")
print (np.mean(income))

#plt.hist(income, 50)
#plt.show()

#Median

print("Showing Median")
print(np.median(income))

ages = np.random.randint(18, high=90, size=500)
print (ages)

print ("Printing Mode")
print (stats.mode(ages))