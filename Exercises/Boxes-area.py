
import numpy as np

def boxArea(boxCorners, area):
    x1=boxCorners[0]
    x2=boxCorners[1]
    x3=boxCorners[2]
    x4=boxCorners[3]
    y1=boxCorners[4]
    y2=boxCorners[5]
    y3=boxCorners[6]
    y4=boxCorners[7]
    A1=(x2-x1)*(y2-y1)
    A2=(x4-x3)*(y4-y3)
    A3=max(0,min(x2,x4)-max(x1,x3))*max(0,min(y2,y4)-max(y1,y3))
    A4=A1+A2-A3
    
    if area == "Box1":
        A = A1
    
    elif area == "Box2":
        A = A2
    
    elif area == "Intersection":
        A = A3
    
    elif area == "Union":
        A = A4
    return A


    



    