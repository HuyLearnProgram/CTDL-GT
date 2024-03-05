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

    # def __init__(self):
    #     self.head = None
    #     self.tail = None
    #     self.length = 0

    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.tail = newNode
        else:
            newNode.next = self.head
        self.head = newNode
        self.length += 1

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        proppedNode = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            preNode = self.head
            while preNode.next is not self.tail:
                preNode = preNode.next
            self.tail = preNode
            preNode.next = None
        self.length -= 1
        return proppedNode

    def popFirst(self):
        if self.length == 0:
            return None
        proppedNode = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            proppedNode.next = None
        self.length -= 1
        return proppedNode

    def delete(self, index):
        preNode = self.head
        if index >= self.length or index <= -1:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length-1:
            return self.pop()
        for _ in range(index-1):
            preNode = preNode.next
        deletedNode = preNode.next
        preNode.next = deletedNode.next
        deletedNode.next = None
        self.length -= 1
        return deletedNode

    def insert(self, index, value):
        newNode = Node(value)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            preNode = self.head
            for _ in range(index-1):
                preNode = preNode.next
            nextNode = preNode.next
            newNode.next = nextNode
            preNode.next = newNode
        self.length += 1

    def get(self, index):
        if index >= self.length or index < 0:
            return None
        tempNode = self.head
        for _ in range(index):
            tempNode = tempNode.next
        return tempNode

    def setValue(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def reverse(self):
        for index in range(self.length//2):
            lastIndex = self.length - 1 - index
            firstNode = self.get(index)
            lastNode = self.get(lastIndex)
            tempValue = firstNode.value
            firstNode.value = lastNode.value
            lastNode.value = tempValue

    def middleNode(self):
        if self.length == 0:
            return None
        if self.head == self.tail:
            return self.head

        newNode = self.head
        for _ in range(self.length//2):
            newNode = newNode.next
        return newNode

    def removeDuplicates(self):
        if self.head is None:
            return
        nodeValues = set()  # set to store unique node values
        currentNode = self.head
        nodeValues.add(currentNode.value)
        while currentNode.next:
            if currentNode.next.value in nodeValues:  # duplicate found
                currentNode.next = currentNode.next.next
                self.length -= 1
            else:
                nodeValues.add(currentNode.next.value)
                currentNode = currentNode.next
        self.tail = currentNode

    # merge two sorted linked list return a sorted linked list

    def mergeTwoSortedLinkedList(self, list1, list2):
        tempList = LinkedList(0)
        if list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        else:
            if list1.next is None:
                while list2:
                    if list1 and list1.value < list2.value:
                        tempList.append(list1.value)
                        list1 = list1.next
                    else:
                        tempList.append(list2.value)
                        list2 = list2.next

            elif list2.next is None:
                while list1:
                    if (list2 and list1.value < list2.value) or not list2:
                        tempList.append(list1.value)
                        list1 = list1.next
                    else:
                        tempList.append(list2.value)
                        list2 = list2.next
            else:
                while list1 and list2:
                    if list1.value < list2.value:
                        tempList.append(list1.value)
                        list1 = list1.next
                    else:
                        tempList.append(list2.value)
                        list2 = list2.next
        tempList.popFirst()
        return tempList.head

    # remove duplicates by head of list
    def removeDuplicatesByHead(self, headOfList):
        newList = LinkedList(0)
        newList.popFirst()
        if not headOfList:
            return None
        while headOfList:
            valueList = newList.values()
            if headOfList.value not in valueList:
                newList.append(headOfList.value)
            headOfList = headOfList.next
        return newList.head

    # remove elements by head of list and value is given
    def removeElements(self, headOfList, val):
        newList = LinkedList(0)
        newList.popFirst()
        if not headOfList:
            return None
        while headOfList:
            if headOfList.value != val:
                newList.append(headOfList.value)
            headOfList = headOfList.next
        return newList.head

    # reverse linked list by head of list
    def reverseLinkedList(self, headOfList):
        newList = LinkedList(0)
        newList.popFirst()
        if not headOfList:
            return None
        while headOfList:
            newList.prepend(headOfList.value)
            headOfList = headOfList.next
        return newList.head

    # Check palindrome linked list by head of list
    def isPalindromeLinkedList(self, headOfList):
        reverseHead = self.reverseLinkedList(headOfList)
        if not headOfList:
            return True
        while headOfList:
            if headOfList.value != reverseHead.value:
                return False
            headOfList = headOfList.next
            reverseHead = reverseHead.next
        return True

    # return the middle node of the linked list by head of list
    def middleNodeLinkedList(self, headOfList):
        lenOfList = 0
        tempNode = headOfList
        while headOfList:
            lenOfList += 1
            headOfList = headOfList.next
        for i in range(lenOfList//2):
            tempNode = tempNode.next
        return tempNode

    # Return a list have all values of linked list node
    def values(self):
        tempList = []
        for index in range(self.length):
            tempList.append(self.get(index).value)
        return tempList

    # Print all node value of linked list by head of linked list
    def printHeadList(self, headOfList):
        tempStr = ""
        while headOfList:
            tempStr += str(headOfList.value) + ","
            headOfList = headOfList.next
        tempStr = tempStr[:-1]
        result = f'[{tempStr}]'
        return result

    def __str__(self):
        tempNode = self.head
        result = ''
        while tempNode is not None:
            result += str(tempNode.value)
            if tempNode.next is not None:
                result += " -> "
            tempNode = tempNode.next
        return result


# list = LinkedList(2)
## Cau 3 Insertion at the Beginnig of a Singly Linked List ##
# list.prepend(1)

## Cau 3 Insertion at the End of a Singly Linked List ##

# list.append(3)
# list.append(4)
# list.append(2)
# list.append(3)
# list.append(4)
# list.append(5)
# list.append(6)

# list.insert(1, 0)
# print(list.__str__())
# print(list.pop().value)
# print(list.popFirst().value)

## Cau 4: Deletion from a Singly Linked List ##

# print(list.delete(1).value)
# print(list.__str__())

## Cau 5 Reverse a Singly Linked List ##

# list.reverse()
# print(list.__str__())

## Cau 6 Middle of a Singly Linked List ##

# print(list.middleNode().value)

## Cau 7 Remove Duplicates from a Singly Linked List ##

# list.removeDuplicates()
# print(list.__str__())

## Cau 8 Merge Two Sorted Linked List ##

# list1 = LinkedList(1)
# list1.popFirst()
# list1.append(2)
# list1.append(4)
# list2 = LinkedList(1)
# list2.popFirst()
# list2.append(3)
# list2.append(4)
# mergeListHead = LinkedList(0).mergeTwoSortedLinkedList(list1.head, list2.head)
# print(LinkedList(0).printHeadList(mergeListHead))

## Cau 9 Remove Duplicates ##
# list1 = LinkedList(1)
# list1.append(1)
# list1.append(2)
# list1.append(3)
# list1.append(3)
# print(list1.__str__())
# removeDupHead = LinkedList(0).removeDuplicates(list1.head)
# print(LinkedList(0).printHeadList(removeDupHead))

## Cau 10 Remove Linked List Elements ##
# list1 = LinkedList(1)
# list1.popFirst()
# list1.append(2)
# list1.append(6)
# list1.append(3)
# list1.append(4)
# list1.append(5)
# list1.append(6)
# val = 6
# list1.append(7)
# list1.append(7)
# list1.append(7)
# list1.append(7)
# val = 7
# removeElementHead = LinkedList(0).removeElements(list1.head, val)
# print(LinkedList(0).printHeadList(removeElementHead))

## Cau 11: Reverse Linked List ##

# list1 = LinkedList(1)
# list1.append(2)
# list1.append(3)
# list1.append(4)
# list1.append(5)
# reverseListHead = LinkedList(0).reverseLinkedList(list1.head)
# print(LinkedList(0).printHeadList(reverseListHead))

## Cau 12: Palindrome Linked List ##

# list1 = LinkedList(1)
# list1.append(2)
# list1.append(2)
# list1.append(1)
# print(LinkedList(0).isPalindromeLinkedList(list1.head))

## Cau 13: Middle of the Linked List ##

# list1 = LinkedList(1)
# list1.append(2)
# list1.append(3)
# list1.append(4)
# list1.append(5)
# list1.append(6)

# middelNode = LinkedList(0).middleNodeLinkedList(list1.head)
# print(middelNode.value)

list = LinkedList(1)
list.append(2)
list.append(2)
list.append(3)
list.append(4)
list.append(4)
list.append(4)
list.append(5)
list.removeDuplicates()
print(list.__str__())
