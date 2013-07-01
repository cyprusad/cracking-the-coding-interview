class Node:
    def __init__(self, num):
        self.val = num

    def nextNode(self, n):
        self.nextNode = n

    def getNext(self):
        return self.nextNode

def getNthToLast(node, n):
    nth = node
    this = node
    for i in range(n-1):
        nth = nth.getNext()
    while nth != None:
        nth = nth.getNext()
        this = this.getNext()
    return this
