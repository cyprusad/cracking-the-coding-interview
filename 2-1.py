# Linked list
class Node:
    def __init__(self, num):
        self.val = num

    def nextNode(self, node):
        self.nextNode = node

    def getNext(self):
        return self.nextNode

# O(n) time
def length(node):
    if node == None:
        return 0
    else:
        return 1 + length(node.getNext())

def remove_dups(node):
    # This is the same thing we did in chapter 1, recursive and with hashtable

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n1.nextNode(n2)
    n2.nextNode(None)
    print length(n1)
