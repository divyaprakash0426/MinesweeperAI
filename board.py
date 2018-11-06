from Cell import *
import random

class MinesBoard(object):


    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.mines_loc = []
        self.mines_loc_set = ()
        self.opened = set()
        self.flagged = set()
        self.surrounded_mines = {}
        self.remaining_mines = mines

        ## Initilize the board
        self.matrix = [[0 for x in range(width)] for y in range(height)]
        for x in range(self.width):
            for y in range(self.height):
                self.matrix[x][y] = Cells(x,y)

        ## Place mines
        self.mines_loc_set = self.place_mines(width, height, self.matrix)


        ## Calc number of mines
        self.CalcNumberOfMines(width, height, self.matrix)

        ## Stores all neighbors in dictionary for sets
        self.neighbors_dictionary = self.neighbors_dic()


    ## printing the grid in a nice format
    def printGrid(self):
        for x in range(self.width):
            for y in range(self.height):
                print("{}  ".format(self.matrix[x][y].visible), end=""),
            print("")

    ## printing the grid in a nice format
    def printGrid2(self):
        for x in range(self.width):
            for y in range(self.height):
                print("{}  ".format(self.matrix[x][y].value), end=""),
            print("")

    ## Check if it is in the range
    def inRange(self, id):
        (x,y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    ## find all neighbors
    def neighbors(self,id):
        movements = [[-1,-1],[-1,0], [-1,+1], [0,1], [+1,+1], [1,0],[+1,-1], [0,-1]]
        result = []
        for moves in movements:
            neighbor = [id.getX() + moves[0], id.getY() + moves[1]]
            if self.inRange(neighbor):
                result.append(self.matrix[neighbor[0]][neighbor[1]])

        return result

    ## Get a dictionaty of neighbor using sets
    def neighbors_dic(self):
        movements = [[-1,-1],[-1,0], [-1,+1], [0,1], [+1,+1], [1,0],[+1,-1], [0,-1]]
        neighbors = {}
        for i in range(self.width):
            for j in range(self.height):
                result = set()
                for moves in movements:
                    neighbor = [self.matrix[i][j].getX() + moves[0], self.matrix[i][j].getY() + moves[1]]
                    if self.inRange(neighbor):
                        result.add(( self.matrix[neighbor[0]][neighbor[1]]))

                        neighbors[self.matrix[i][j]] = result

        return neighbors


    ## Place mines randomly
    def place_mines(self, width, height, board):
        mines = self.mines
        mines_location = set()
        while( mines > 0):
            x = random.randrange(width)
            y = random.randrange(height)
            if board[x][y].status == False:
                board[x][y].status = True
                board[x][y].value = 9
                self.mines_loc.append(board[x][y])
                mines_location.add(board[x][y])
            mines -=1

        return mines_location



    ### Calculate the number of cells whether it has a mine or not
    def CalcNumberOfMines(self, width, height, board):

        mines_cell = 0
        for i in range(width):
            for j in range(height):
                neighbor = self.neighbors(board[i][j])
                length = len(neighbor)
                mines_cell = 0
                for d in range(length):
                    if(neighbor[d].status == True):
                        mines_cell +=1

                if board[i][j].status != True:
                    board[i][j].value = mines_cell

    ## Just a greed function to open all zeros
    def opening_all_zeros(self, intital_cell):
        x = intital_cell.getX()
        y = intital_cell.getY()
        neighbor_sets = ()
        new_matrix = self.matrix

        if not self.matrix[x][y].isVisited:
            self.matrix[x][y].isVisited = True
            if self.matrix[x][y].value != 0:
                return
            neighbor_sets = self.neighbors(self.matrix[x][y])
            if len(neighbor_sets) != 0:
                for neighbor in neighbor_sets:
                    if neighbor.value == 0 or neighbor.value != 9:
                        self.opening_all_zeros(neighbor)


    ## The actual algorithm
    def open_cell(self, cell):
        (x,y) = cell.getX(), cell.getY()
        if cell not in self.opened:
            self.opened.add(cell)
            cell.visible = cell.value
            print("\n")
            print("I am opening {}".format((x,y)))
            print("\n")
            self.printGrid()
            if(self.IsGameOver(cell)):
                self.surrounded_mines[cell] = 9
                print("\n******* Dead *******\n")
                print("The Actual Board")
                self.printGrid2()
                exit()

            else:
                # if it is not a mine we show the value inside that cell - the clue number
                self.surrounded_mines[cell] = cell.value

        ## if it is not in the opened sets, we ignore it
        else:
            return

    ## add these to a flag set
    def flag(self, cell):
        self.flagged.add(cell)
        cell.visible = 'F'
        self.remaining_mines -=1
        print("\n")
        print("I am flagging {}".format((cell.getX(), cell.getY())))
        print("\n")
        self.printGrid()
        # print("The remaining_mines are {} ".format(self.remaining_mines))

    # Check if we cliked on a mine or not
    def IsGameOver(self, cell):
        if (cell) in self.mines_loc_set:
            return True
