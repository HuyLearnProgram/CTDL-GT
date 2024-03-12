class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return True

    def popFirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def setValue(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        # if index >= self.length or index < 0:
        #     return None

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
            preNode.next = newNode
            self.length += 1


myLinkedList = LinkedList(1)
myLinkedList.append(3)


print('LL before insert():')
myLinkedList.printList()


myLinkedList.insert(1, 2)

print('\nLL after insert(2) in middle:')
myLinkedList.printList()


myLinkedList.insert(0, 0)

print('\nLL after insert(0) at beginning:')
myLinkedList.printList()


myLinkedList.insert(4, 4)

print('\nLL after insert(4) at end:')
myLinkedList.printList()


"""
    EXPECTED OUTPUT:
    ----------------
    LL before insert():
    1
    3

    LL after insert(2) in middle:
    1
    2
    3

    LL after insert(0) at beginning:
    0
    1
    2
    3

    LL after insert(4) at end:
    0
    1
    2
    3
    4

"""
