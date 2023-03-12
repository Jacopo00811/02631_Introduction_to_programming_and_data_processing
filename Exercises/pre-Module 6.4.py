import pandas as pd
import numpy as np

topscorers = pd.read_csv("topscorers_small.csv")
print(topscorers)
print("\n")

print(topscorers.columns)
print(topscorers.columns[1])
print("\n")

print(topscorers.Goals)
A = np.array(topscorers.Goals)
print(A)
print("\n")


All = np.array(topscorers)
print(All) # is all covertet to a np array
print("\n")


print(np.array(topscorers.MinutesPlayed) / np.array(topscorers.Goals))
print("\n")


print(topscorers.Player)
print("\n")

print(topscorers.Goals[3])
print("\n")

print(topscorers.iloc[:,3])
print("\n")

print(np.array(topscorers.iloc[:,3]))
print("\n")
print("\n")



print(All[1][1])
print("\n")
print("\n")



letter_frequencies = np.array(pd.read_csv("letter_frequencies.csv"))
print(letter_frequencies[0][1])
