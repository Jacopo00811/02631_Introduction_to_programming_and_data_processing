import numpy as np

def computeItemCost(resourceItemMatrix, resourceCost):

    #itemCost = np.dot(resourceItemMatrix.T , resourceCost)
    itemCost = np.dot(resourceCost , resourceItemMatrix)
    return itemCost

print(computeItemCost(np.array([[6,3,0],[17,11,9],[4,2,12]]),
np.array([101.25,84.00,75.50])))