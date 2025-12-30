class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, data):
        node = Node(data)
        self.first = node
        self.last = node
        self.length = 1

    def print_queue(self):
        print(">>>>>>>>>>>>")
        st_str = ""
        temp = self.first
        while temp:
            st_str = str(temp.data) + "<" + st_str
            temp = temp.next
        print(st_str)

    def enqueue(self, data):
        new_node = Node(data)
        self.last.next = new_node
        self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        self.first = temp.next
        temp.next = None
        self.length -= 1


st1 = Queue(1)
st1.enqueue(2)
st1.enqueue(3)
st1.print_queue()
st1.dequeue()
st1.print_queue()