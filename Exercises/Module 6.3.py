import numpy as np
import string

def letterFrequency(filename):
    
   filein = open(filename,"r")
   lines = filein.readlines()
   smalltext = "".join(lines)
   smalltext = smalltext.lower()
   
   total_letters = np.array([])
   freq = np.array([])
   alphabet = np.array(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
   
   smalltext.replace(" ","")
   
   

   table = str.maketrans(",.;:!?","      ",string.punctuation)   
   smalltext = [w.translate(table) for w in smalltext]
   print(smalltext)
   
   total_letters = len(smalltext)
   
   for i in alphabet:
       
       letter = smalltext.count(i)
       #total_letters = np.append(letter)
       x = letter/total_letters*100
       freq = np.append(freq, x)
       
   return freq 
    
print(letterFrequency("small_text.txt"))