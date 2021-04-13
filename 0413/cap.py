class Cap:
    def __init__(self):
        self._color = "empty"

    def checkColor(self):
        return self._color

    def changeColor(self,color):
        self._color = color

    def getSymbol(self):
        if self._color == "empty":
            return " "
        elif self._color == "red":
            return "R"
        else:
            return "Y"


