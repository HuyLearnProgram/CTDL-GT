class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        newNode = Node(value)
        self.top = newNode
        self.height = 1

    def printStack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        newNode = Node(value)
        if self.height == 0:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.height += 1
        return True

    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        return temp


myStack = Stack(4)
myStack.push(3)
myStack.push(2)
myStack.push(1)

print('Stack before pop():')
myStack.printStack()

print('\nPopped node:')
print(myStack.pop().value)

print('\nStack after pop():')
myStack.printStack()


"""
    EXPECTED OUTPUT:
    ----------------
    Stack before pop():
    1
    2
    3
    4

    Popped node:
    1

    Stack after pop():
    2
    3
    4

"""
