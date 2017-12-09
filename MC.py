#Import libraries
import numpy as np
import math as math
n = 10000
def Monte_Carlo(n):
    return np.mean(np.exp(np.random.uniform(0,1,n)))
print Monte_Carlo(n)