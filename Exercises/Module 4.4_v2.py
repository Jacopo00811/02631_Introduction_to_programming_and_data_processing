import numpy as np 

def clusterAnalysis(reflectance):
    even_numbered = np.array([])
    odd_numbered = np.array([])
    average_class_1 = 0
    average_class_2 = 0
    clusterAssignments = np.array([])
    average_e = 0
    average_o = 0
    j = 0
    
    for i in range(0, len(reflectance)):
       
        if i % 2 == 0:
            even_numbered.append(reflectance[i])
        else:
            odd_numbered.append(reflectance[i])


    for element in even_numbered:
        average_e = average_e + element
    
        average_e = average_e/len(even_numbered)
    
            
    for element in odd_numbered:
        average_o = average_o + element
    
        average_o = average_o/len(odd_numbered)
        
    average_class_1 = odd_numbered.copy()
    average_class_2 = even_numbered.copy()
    
    
    
    
    
    for element in reflectance:
        
            if abs(element - average_e) < abs(element - average_o):
                even_numbered[i] = element
                i += 1
            else: 
                odd_numbered[j] = element
                j += 1