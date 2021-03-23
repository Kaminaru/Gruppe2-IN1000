class Node:
    def __init__(self, newData): # nytt er data
        self._data = newData
        self._next = None

    def setNext(self, nextNode):
        self._next = nextNode

    def getNext(self):
        return self._next

    def getData(self) :
        return self._data

    # def __str__(self):
    #     return f"I am '{self._data}'"