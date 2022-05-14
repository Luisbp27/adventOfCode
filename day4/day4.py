import csv
import numpy

class Board:

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.board = [[0 for i in range(columns)] for j in range(rows)]

    def __toString__(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.board[i][j], end=" ")

def __main__():
    with open("numbers.txt", "r", encoding="utf-8") as f:
        numbers = list(csv.reader(f, delimiter=','))
    
    
    



if __name__ == '__main__':
    __main__()