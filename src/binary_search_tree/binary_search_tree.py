class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    Binary Search Tree always has the left nodes < right nodes
    """

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

    def BFS(self):
        queue = [self.root]
        bst_list = []
        while len(queue) > 0:
            current = queue.pop(0)
            bst_list.append(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return bst_list


bst = BinarySearchTree(5)
print(bst.insert(5))
print(bst.insert(10))
print(bst.insert(1))
print(bst.search(10))
print(bst.search(6))

my_tree = BinarySearchTree(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())