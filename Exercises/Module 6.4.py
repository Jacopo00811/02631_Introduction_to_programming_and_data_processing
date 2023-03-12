import numpy as np
import pandas as pd

def computeLanguageError(freq):

    letter_frequencies = np.array(pd.read_csv("letter_frequencies.csv"))
    E = np.array([])
    
    for j in range(1,16):
        somma = 0 
        for i in range(len(freq)):
            somma = somma + pow(freq[i] - letter_frequencies[i][j], 2)
        
        E = np.append(E, somma)
        
    return E

print(computeLanguageError(np.array([8.101852, 2.237654,
2.469136, 4.552469, 12.345679, 2.006173, 1.929012,
6.712963, 7.175926, 0.077160, 1.157407, 3.395062,
1.080247, 6.712963, 7.870370, 1.466049, 0.077160,
6.018519, 5.401235, 10.956790, 2.854938, 0.925926,
2.932099, 0.000000, 1.543210, 0.000000])))