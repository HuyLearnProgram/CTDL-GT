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


myDoublyLinkedList = DoublyLinkedList(7)

print('Head:', myDoublyLinkedList.head.value)
print('Tail:', myDoublyLinkedList.tail.value)
print('Length:', myDoublyLinkedList.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 7
    Tail: 7
    Length: 1

"""
