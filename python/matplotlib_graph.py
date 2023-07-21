#Graph
import matplotlib.pyplot as plt
import numpy as np
a = np.linspace(0,10,100)
b = np.exp(-a)
plt.plot(a,b)
plt.show()

#Histogram
from numpy.random import normal,rand
x = normal(size =200)
plt.hist(x,bins = 30)
plt.show()
