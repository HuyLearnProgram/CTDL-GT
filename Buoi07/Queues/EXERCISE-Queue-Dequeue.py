class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        newNode = Node(value)
        self.first = newNode
        self.last = newNode
        self.length = 1

    def printQueue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        newNode = Node(value)
        if self.first is None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return True

    def dequeue(self):
        if self.last is None:
            return None
        temp = self.first
        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1
        return temp


myQueue = Queue(1)
myQueue.enqueue(2)

# (2) Items - Returns 2 Node
print(myQueue.dequeue().value)
# (1) Item -  Returns 1 Node
print(myQueue.dequeue().value)
# (0) Items - Returns None
print(myQueue.dequeue())


"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    None

"""
