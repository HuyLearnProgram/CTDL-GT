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
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1
        return True


myDoublyLinkedList = DoublyLinkedList(2)
myDoublyLinkedList.append(3)

print('Before prepend():')
print('----------------')
print('Head:', myDoublyLinkedList.head.value)
print('Tail:', myDoublyLinkedList.tail.value)
print('Length:', myDoublyLinkedList.length, '\n')
print('Doubly Linked List:')
myDoublyLinkedList.printList()


myDoublyLinkedList.prepend(1)


print('\n\nAfter prepend():')
print('---------------')
print('Head:', myDoublyLinkedList.head.value)
print('Tail:', myDoublyLinkedList.tail.value)
print('Length:', myDoublyLinkedList.length, '\n')
print('Doubly Linked List:')
myDoublyLinkedList.printList()


"""
    EXPECTED OUTPUT:
    
    Before prepend():
    ----------------
    Head: 2
    Tail: 3
    Length: 2 

    Doubly Linked List:
    2
    3


    After prepend():
    ---------------
    Head: 1
    Tail: 3
    Length: 3 

    Doubly Linked List:
    1
    2
    3

"""
