import math
import numpy as np

def circleAreaMC(xvals, yvals):  
    
    n = 0  # number of points in the circle 
   
    for i in range(0, len(xvals)):
        if math.sqrt(pow(xvals[i], 2) + pow(yvals[i], 2)) <= 1:
            n += 1
       
    A = 4*n/len(xvals)   # 4 = area of a square with l/2 = 1
    
    return A


print(circleAreaMC(np.array([-0.1, 0.7, 0.8, 0.5, -0.4]), np.array([0.3, -0.1, 0.9, 0.6, -0.3])))

