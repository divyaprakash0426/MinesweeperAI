
from Cell import *
from board import *
import random


def printGrid(matrix, width, height, attr):
    for x in range(width):
        for y in range(height):
            print("{} ,".format(matrix[x][y].__dict__[attr])),
        print("")


dim = 4
mines = 3
game = MinesBoard(dim,dim, mines)
# print("\n Mines Matrix \n")
# printGrid(game.matrix, dim, dim, 'status')

print("\n Mines and it is surroundings \n")
printGrid(game.matrix, dim, dim, 'value')
# printGrid(game.matrix, dim, dim, 'isVisited')


node = game.matrix[0][0]

print(int(node.value))
