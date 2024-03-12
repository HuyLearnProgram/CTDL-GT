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


myDoublyLinkedList = DoublyLinkedList(1)
myDoublyLinkedList.append(2)


print('Head:', myDoublyLinkedList.head.value)
print('Tail:', myDoublyLinkedList.tail.value)
print('Length:', myDoublyLinkedList.length, '\n')

print('Doubly Linked List:')
myDoublyLinkedList.printList()


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Doubly Linked List:
    1
    2
    
"""
