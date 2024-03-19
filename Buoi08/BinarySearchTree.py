class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return True
        else:
            temp = self.root
            newNode = Node(value)
            while temp is not None:
                if newNode.value < temp.value:
                    if temp.left is None:
                        temp.left = newNode
                        return True
                    else:
                        temp = temp.left
                elif newNode.value > temp.value:
                    if temp.right is None:
                        temp.right = newNode
                        return True
                    else:
                        temp = temp.right
                else:
                    return False

    def contains(self, treeNode):
        val = treeNode.value
        temp = self.root
        if self.root is None:
            return False
        else:
            while temp is not None:
                if val < temp.value:
                    temp = temp.left
                elif val > temp.value:
                    temp = temp.right
                else:
                    return True
        return False

    def preOrderTraverse(self, treeNode):
        if treeNode is None:
            return
        print(treeNode.value)
        self.preOrderTraverse(treeNode.left)
        self.preOrderTraverse(treeNode.right)


bst = BinarySearchTree()
bst.insert(4)
bst.insert(3)
bst.insert(5)
bst.insert(1)
bst.insert(2)
bst.preOrderTraverse(bst.root)
print(bst.contains(Node(3)))
