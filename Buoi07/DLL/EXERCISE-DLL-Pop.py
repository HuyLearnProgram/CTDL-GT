class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
        return True

    def pop(self):
        temp = self.tail
        if self.head is None:
            return None
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp


myDoublyLinkedList = DoublyLinkedList(1)
myDoublyLinkedList.append(2)


# (2) Items - Returns 2 Node
print(myDoublyLinkedList.pop().value)
# (1) Item -  Returns 1 Node
print(myDoublyLinkedList.pop().value)
# (0) Items - Returns None
print(myDoublyLinkedList.pop())


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
