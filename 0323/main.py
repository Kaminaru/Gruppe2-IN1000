from node import Node
from linkedlist import LinkedList

# Reverse adding of new element to linkedList:

def printMyLinkedList(start):
    """Prints out data for each node in linkedlist"""
    n = start
    while n != None:
        print(n.getData())
        n = n.getNext()


print("--------------EXAMPLE 1----------------")
# EXAMPLE 1: add manually
start = None
new = Node("A")
new._next = start   # Not the right way to do it if we want to do Object-oriented programming
                    # Because we know that ._next is "privat"
# ny.setNext(start) # good way to do it
start = new # Start points to node with data = "A"

new = Node("B")
new.setNext(start)
start = new
new = Node("C")
new.setNext(start)
start = new
new = Node("D")
new.setNext(start)
start = new

printMyLinkedList(start)


print("--------------EXAMPLE 2----------------")
# EXAMPLE 2: add with for-loop
start = None
for letter in 'ABCDEFG':
    ny = Node(letter)
    ny.setNext(start)
    start = ny


printMyLinkedList(start)

print("--------------EXAMPLE 3----------------")
# EXAMPLE 3: use new class that have push, pop functions
linkedlist1 = LinkedList()
for letter in 'ABCD':
    linkedlist1.push(letter)

#linkedlist1.printWhole()

while linkedlist1.notEmpty():
    print(linkedlist1.pop())


linkedlist2 = LinkedList()

for text in ["snart", "over", "er", "pandemien", "håper"]:
    linkedlist2.push(text)

while linkedlist2.notEmpty():
    print(linkedlist2.pop())
