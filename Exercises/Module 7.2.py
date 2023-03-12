import numpy as np

def textToNato(plainText):
    
    plainText = plainText.lower()
    alphabet = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    natoAlphabet = np.array([ "Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "Xray", "Yankee", "Zulu"])
    Text = np.array([])
    
    
    for i in range(len(plainText)):
        for letter in alphabet:
           
           if plainText[i] == letter:
               for word in natoAlphabet:
                   
                   if word[0] == letter.upper():
                       Text = np.append(Text, word)
                       print(Text)
    natoText = '-'.join(str(item) for item in Text)
    
    return natoText

print(textToNato("hello"))