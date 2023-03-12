import numpy as np

def letterFrequency(filename):
    
    filein=open(filename, "r")
    lines=filein.readlines()
    smalltext="".join(lines)
    smalltext=smalltext.lower()
  
    alphabet = np.array(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
    frequency = np.array([])
    
    for i in alphabet:
        frequency = np.append(frequency,smalltext.count(i))
    
    total_letters = np.sum(frequency)
    freq = (frequency/total_letters)*100
        

    return freq

print(letterFrequency("small_text.txt"))

