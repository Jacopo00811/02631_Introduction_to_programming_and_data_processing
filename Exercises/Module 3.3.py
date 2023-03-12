import numpy as np
import math 

def acuteAngle(v1, v2):
    theta = math.acos(np.dot(v1, v2))
    if theta > math.pi/2:
        theta = math.pi - theta
        
    return theta

print(acuteAngle(np.array([-4.0/5.0, 3.0/5.0]), np.array([20.0/29.0, 21.0/29.0])))
    