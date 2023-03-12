import numpy as np

def computePassesGoalLine(point, directionVector):
   Xc = 105
 
   if directionVector[0] > 0 :
       y = point[1] + (directionVector[1]/directionVector[0])*(Xc-point[0])
      
   elif directionVector[0] < 0 :
       y = point[1] - (directionVector[1]/directionVector[0])*(point[0])
    
   elif directionVector[0] == 0 :
       return False
  
   if y > 30.34 and y < 37.66 :
        score = True
   else:
        score = False
   
   return score


#print(computePassesGoalLine(np.array([30, 20]), np.array([10, 2])))

print(computePassesGoalLine(np.array([50, 50]), np.array([0, 1])))