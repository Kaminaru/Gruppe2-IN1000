from cap import Cap

class Board:
    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._gameBoard = [] # empty at the start

        for i in range(self._row):
            tmprow = []
            for j in range(self._col):
                tmprow.append(Cap())
            self._gameBoard.append(tmprow)


    def play(self):
        player = 0 # first player starts the game
        print(f"!!! Player {player} turn !!!")

        self.showBoard()
        try:
            colNumber = int(input(f"Choose column number you want to put cap on: (from 0 to {self._col-1}) "))
            print("Or write -1 to stop the game")
        except:
            print("Wrong input")
            colNumber = -1

        while colNumber != -1 and colNumber < self._col:
            if self._gameBoard[0][colNumber].checkColor() == "empty":
                self.dropCap(colNumber, player)
                if self.checkWin(player): # because we don't need to check other player color, we have checked it before (saves time)
                    self.showBoard()
                    print(f"Player {player} won!")
                    break
                if player == 0:
                    player = 1
                else:
                    player = 0
                print(f"!!! Player {player} turn !!!")
            else:
                print("No place in this column")
            self.showBoard()
            try:
                colNumber = int(input(f"Choose column number you want to put cap on: (from 0 to {self._col-1}) "))
                print("Or write -1 to stop the game")
            except:
                print("Wrong input")
                colNumber = -1

    def showBoard(self):
        printText = " |"
        for num in range(self._col):
            printText += f"{num}|"
        printText += "\n"

        for i in range(self._row):
            printText += f"{i}|"
            for j in range(self._col):
                printText += self._gameBoard[i][j].getSymbol() + "|"
            printText += "\n"
        print(printText)

    def dropCap(self, colNum, player):
        bottom = self._row - 1
        while self._gameBoard[bottom][colNum].checkColor() != "empty":
            bottom -= 1

        if player == 0:
            self._gameBoard[bottom][colNum].changeColor("red")
        else:
            self._gameBoard[bottom][colNum].changeColor("yellow")



    def checkWin(self, player):
        if player == 0:
            color = "red"
        else:
            color = "yellow"

        # check row line
        counter = 0
        for i in range(self._row):
            for j in range(self._col):
                if self._gameBoard[i][j].checkColor() == color:
                    counter += 1
                else:
                    counter = 0
                if counter == 4: # we have winner
                    return True
            counter = 0

        # check column line
        counter = 0
        for j in range(self._col):
            for i in range(self._row):
                if self._gameBoard[i][j].checkColor() == color:
                    counter += 1
                else:
                    counter = 0
                if counter == 4: # we have winner
                    return True
            counter = 0

        # extra check x-check
        # \ , bottom up
        counter = 0
        for i in range(self._row - 1, -1, -1):
            for j in range(self._col):
                if i+j <= self._row - 1:
                    if self._gameBoard[i+j][j].checkColor() == color:
                        counter += 1
                    else:
                        counter = 0
                    if counter == 4: # we have winner
                        return True
            counter = 0


        # /
        for i in range(self._row - 1, -1, -1):
            for j in range(self._col - 1, -1, -1):
                for k in range(self._row):
                    if i-k > 0 and j+k <= self._col - 1:
                        if self._gameBoard[i-k][j+k].checkColor() == color:
                            counter += 1
                        else:
                            counter = 0
                        if counter == 4: # we have winner
                            return True
            counter = 0

        return False
