class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        newNode = Node(value)
        self.top = newNode
        self.height = 1


myStack = Stack(4)

print('Top:', myStack.top.value)
print('Height:', myStack.height)


"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""
