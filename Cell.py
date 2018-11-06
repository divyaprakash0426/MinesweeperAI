class Cells:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = False  ## check if does have a mine or not
        self.isVisited = False ## opened or not. the user or the computer
        self.flagged = False ## marked or not. Selected as having a mine
        self.value = 0
        self.visible= "-"


    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def visited(self):
        if self.isVisited:
            return self.value
        else:
            return "#"
