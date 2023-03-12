import numpy as np 

def clusterAnalysis(reflectance):
    even_numbered = np.array([])
    odd_numbered = np.array([])
    class_1 = np.array([])
    class_2 = np.array([])
    clusterAssignments = np.array([])
    average_e = 0
    average_o = 0 
    
    for i in range(0, len(reflectance)):
       
        if i % 2 == 0:
            even_numbered.append(reflectance[i])
        else:
            odd_numbered.append(reflectance[i])
    
    
    i = 0
    j = 0
    
    
    while True:
        
        class_1 = odd_numbered.copy()
        class_2 = even_numbered.copy()
    
        for element in even_numbered:
            average_e = average_e + element
    
        average_e = average_e/len(even_numbered)
    
            
        for element in odd_numbered:
            average_o = average_o + element
    
        average_o = average_o/len(odd_numbered)
    
        
        
        
        for element in reflectance:
        
            if abs(element - average_e) < abs(element - average_o):
                even_numbered[i] = element
                i += 1
            else: 
                odd_numbered[j] = element
                j += 1
        
        if class_1.np.array_equal == odd_numbered.np.array_equal and class_2.np.array_equal == even_numbered.np.array_equal:
            False
    
    for element in odd_numbered:
        
            clusterAssignments = class_1
        


    return clusterAssignments




print(clusterAnalysis(np.array([1.7, 1.6, 1.3, 1.3, 2.8, 1.4,
2.8, 2.6, 1.6, 2.7])))