# sudoku raw
import numpy as np

def fillSudokuRow (row):
    summatory = 45
    i = 0
    index = 0
    for number in row:
        summatory = summatory - number
        if number == 0:
            index = i 
        i += 1
        
    row[index] = summatory
    return row  

print(fillSudokuRow(row=[9, 4, 0, 1, 5, 7, 2, 3, 8]))