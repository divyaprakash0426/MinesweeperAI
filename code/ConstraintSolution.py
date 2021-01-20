import board
from Cell import *
from board import *
import random
import sys

# The is class is used to find the solution using KB
sys.setrecursionlimit(10000)

class ConstraintSolution(MinesBoard):

    def __init__(self, width, height, mines):
        MinesBoard.__init__(self, width, height, mines)


    def open_cell(self, cell):
        x, y = cell.getX(), cell.getY()
        if cell in self.opened:
            return
        super(ConstraintSolution, self).open_cell(cell)
        self.updateConstraint(cell)
        for n in self.neighbors_dictionary[cell]:
            self.updateConstraint(n)

        # # Random 
        # safe = len(self.neighbors_dictionary[cell] - (self.opened - self.flagged))
        # if safe > cell.value:
        #     self.click_random(cell)



    def updateConstraint(self, cell):
        x, y = cell.getX(), cell.getY()
        if cell not in self.opened:
            return

        if self.surrounded_mines[cell] == len(self.neighbors_dictionary[cell] & self.flagged):
            safe_cells = self.neighbors_dictionary[cell] - self.flagged
            for n in safe_cells:
                self.open_cell(n)
            return

        if self.surrounded_mines[cell] == len(self.neighbors_dictionary[cell] - self.opened):
            suspicious_cell = self.neighbors_dictionary[cell] - self.opened
            for n in suspicious_cell:
                self.flag(n)


    def flag(self, cell):
        x, y = cell.getX(), cell.getY()
        if cell not in self.flagged:
            super(ConstraintSolution, self).flag(cell)
            for n in self.neighbors_dictionary[cell]:
                self.updateConstraint(n)
        else:
            return


    def click_random(self, cell):
        elig = []
        for n in self.neighbors_dictionary[cell]:
            if (n not in self.opened) and (n not in self.flagged):
                    elig.append(n)
        if elig:
            choice = random.choice(elig)
            self.open_cell(choice)
        return




if __name__ == '__main__':

    def printGrid(matrix, width, height, attr):
        for x in range(width):
            for y in range(height):
                print("{}  ".format(matrix[x][y].__dict__[attr]), end ="")
            print("")

    dim = 9
    dim2 = 9
    mines = 10

    game = ConstraintSolution(dim,dim2, mines)


    # print("\n")
    node = game.matrix[0][0]
    game.open_cell(node)

    print("\n")
    print("The Actual Board ")
    printGrid(game.matrix, dim, dim2, 'value')
