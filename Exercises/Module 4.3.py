import numpy as np

def removeIncomplete(id):

    idList = list(np.floor(id)) #creates an idList with all the decimal=0
    idComplete = np.array([])
    
    for i in range(len(id)):
        if idList.count(idList[i]) >= 3:
            idComplete = np.append(idComplete, id[i])
    
    return idComplete

print(removeIncomplete(np.array([1.3, 2.2, 2.3, 4.2, 5.1,
3.2, 5.3, 3.3, 2.1, 1.1, 5.2, 3.1])))