from scipy.ndimage.interpolation import shift
import numpy as np

def movingAvg(y):
  r1 = shift(y, -2, cval=0)
  r2 = shift(y, -1, cval=0)
  r3 = y
  r4 = shift(y, 1, cval=0)
  r5 = shift(y, 2, cval=0)
  
  ysmooth =np.vstack((r1,2*r2,3*r3,2*r4,r5))
  
  ysmooth = (np.sum(ysmooth, axis=0))/9
  
  return ysmooth

print(movingAvg(np.array([0.8, 0.9, 0.7, 0.6, 0.3, 0.4])))  