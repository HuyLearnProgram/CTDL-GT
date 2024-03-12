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
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1
        return True

    def popFirst(self):
        temp = self.head
        if self.head is None:
            return None
        if self.length == 1:
            self.head = self.tail = None
            return temp
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp


myDoublyLinkedList = DoublyLinkedList(2)
myDoublyLinkedList.append(1)


# (2) Items - Returns 2 Node
print(myDoublyLinkedList.popFirst().value)
# (1) Item -  Returns 1 Node
print(myDoublyLinkedList.popFirst().value)
# (0) Items - Returns None
print(myDoublyLinkedList.popFirst())


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
