class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node

    def insert(self, value):
        new_node = Node(value)
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right

    def search(self, value):
        temp = self.root
        while(temp):
            if value == temp.value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right

        return False

bst = BinarySearchTree(5)
print(bst.insert(5))
print(bst.insert(10))
print(bst.insert(1))
print(bst.search(10))
print(bst.search(6))