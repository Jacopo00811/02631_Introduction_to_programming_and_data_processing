import numpy as np

def fermentationRate(measuredRate, lowerBound, upperBound):
    i = 0
    averageRate = 0
    
    for rate in measuredRate:
        if rate <= lowerBound or rate >= upperBound:
            averageRate = averageRate
        else:
            averageRate = averageRate + rate
            i += 1
    averageRate = averageRate/i       
    return averageRate

print(fermentationRate(np.array([20.1, 19.3, 1.1, 18.2, 19.7, 121.1, 20.3, 20.0]), 15, 25))