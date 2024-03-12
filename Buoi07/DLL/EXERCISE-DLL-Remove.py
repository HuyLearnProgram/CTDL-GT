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
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        newNode = Node(value)
        before = self.get(index - 1)
        after = before.next

        newNode.prev = before
        newNode.next = after
        before.next = newNode
        after.prev = newNode

        self.length += 1
        return True

    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            temp = self.popFirst()
            return temp
        if index == self.length - 1:
            temp = self.pop()
            return temp
        else:
            temp = self.get(index)
            preNode = temp.prev
            nextNode = temp.next
            preNode.next = nextNode
            nextNode.prev = preNode
            temp.next = temp.prev = None
            self.length -= 1
            return temp


myDoublyLinkedList = DoublyLinkedList(1)
myDoublyLinkedList.append(2)
myDoublyLinkedList.append(3)
myDoublyLinkedList.append(4)
myDoublyLinkedList.append(5)

print('DLL before remove():')
myDoublyLinkedList.printList()

print('\nRemoved node:')
print(myDoublyLinkedList.remove(2).value)
print('DLL after remove() in middle:')
myDoublyLinkedList.printList()

print('\nRemoved node:')
print(myDoublyLinkedList.remove(0).value)
print('DLL after remove() of first node:')
myDoublyLinkedList.printList()

print('\nRemoved node:')
print(myDoublyLinkedList.remove(2).value)
print('DLL after remove() of last node:')
myDoublyLinkedList.printList()


"""
    EXPECTED OUTPUT:
    ----------------
    DLL before remove():
    1
    2
    3
    4
    5

    Removed node:
    3
    DLL after remove() in middle:
    1
    2
    4
    5

    Removed node:
    1
    DLL after remove() of first node:
    2
    4
    5

    Removed node:
    5
    DLL after remove() of last node:
    2
    4

"""
