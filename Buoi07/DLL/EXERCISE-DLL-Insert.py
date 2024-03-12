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
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def setValue(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index > self.length or index < 0:
            return None

        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            newNode = Node(value)
            preNode = self.head
            for _ in range(index-2):
                preNode = preNode.next

            nextNode = preNode.next
            newNode.next = nextNode
            nextNode.prev = newNode

            preNode.next = newNode
            newNode.prev = preNode
            self.length += 1


myDoublyLinkedList = DoublyLinkedList(1)
myDoublyLinkedList.append(3)


print('DLL before insert():')
myDoublyLinkedList.printList()


myDoublyLinkedList.insert(1, 2)

print('\nDLL after insert(2) in middle:')
myDoublyLinkedList.printList()


myDoublyLinkedList.insert(0, 0)

print('\nDLL after insert(0) at beginning:')
myDoublyLinkedList.printList()


myDoublyLinkedList.insert(4, 4)

print('\nDLL after insert(4) at end:')
myDoublyLinkedList.printList()


"""
    EXPECTED OUTPUT:
    ----------------
    DLL before insert():
    1
    3

    DLL after insert(2) in middle:
    1
    2
    3

    DLL after insert(0) at beginning:
    0
    1
    2
    3

    DLL after insert(4) at end:
    0
    1
    2
    3
    4

"""
