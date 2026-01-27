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

    def invert_bt(self, node: Node):
        root = node
        if root is None:
            return None
        left_node = root.left
        right_node = root.right
        root.left, root.right = right_node, left_node
        self.invert_bt(left_node)
        self.invert_bt(right_node)
        return self.root

    def print_tree(self):
        queue = [self.root]
        bst_list = []
        while len(queue) > 0:
            current = queue.pop(0)
            bst_list.append(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        print(bst_list)

my_tree = BinarySearchTree(1)
my_tree.insert(2)
my_tree.insert(3)
my_tree.insert(4)
my_tree.insert(5)
my_tree.insert(6)
my_tree.insert(7)
my_tree.print_tree()
invrt_root = my_tree.invert_bt(my_tree.root)
my_tree.print_tree()

