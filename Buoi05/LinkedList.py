class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


newNode = Node(10)
print(newNode)

newLinkList = LinkedList(10)
print(newLinkList.head.value)
