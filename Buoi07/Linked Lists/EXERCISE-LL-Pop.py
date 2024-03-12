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
        if self.tail is None:
            return None
        if self.head == self.tail:
            temp = self.head
            self.head = self.tail = None
            return temp
        temp = self.head
        for _ in range(self.length-2):
            temp = temp.next
        self.tail = temp
        tailNode = temp.next
        temp.next = None
        return tailNode


myLinkedList = LinkedList(1)
myLinkedList.append(2)

# (2) Items - Returns 2 Node
print(myLinkedList.pop().value)
# (1) Item -  Returns 1 Node
print(myLinkedList.pop().value)
# (0) Items - Returns None
print(myLinkedList.pop())


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
