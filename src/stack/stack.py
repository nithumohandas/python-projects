class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, data):
        node = Node(data)
        self.top = node
        self.length = 1

    def print_stack(self):
        print(">>>>>>>>>>>>")
        st_str = ""
        temp = self.top
        while temp:
            st_str = st_str + ">" + str(temp.data)
            temp = temp.next
        print(st_str)

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.length -= 1


st1 = Stack(1)
st1.push(2)
st1.push(3)
st1.print_stack()
st1.pop()
st1.print_stack()