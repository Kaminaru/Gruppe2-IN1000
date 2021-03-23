from node import Node

# LIFA (Last in, first out)
class LinkedList:
    def __init__(self) :
        self._list = None # actually it is the start node
                          # and not "whole" linkedlist

    def push(self, data):
        """adds new node at the start"""
        ny = Node(data)
        ny.setNext(self._list)
        self._list = ny

    def pop(self):
        """Removes first node"""
        out = self._list.getData()
        self._list = self._list.getNext()
        return out

    def notEmpty(self):
        return self._list != None

    def printWhole(self):
        n = self._list
        while n != None:
            print(n._data)
            n = n.getNext()