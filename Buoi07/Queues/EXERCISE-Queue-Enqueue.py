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
        if self.last is None:
            self.first = self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return True


myQueue = Queue(1)

print('Queue before enqueue(2):')
myQueue.printQueue()

myQueue.enqueue(2)

print('\nQueue after enqueue(2):')
myQueue.printQueue()


"""
    EXPECTED OUTPUT:
    ----------------
    Queue before enqueue(2):
    1

    Queue after enqueue(2):
    1
    2

"""
