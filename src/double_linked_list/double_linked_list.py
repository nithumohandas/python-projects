class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        print(">>>>>>>>>>>>")
        ll_str = ""
        temp = self.head
        while temp is not None:
            ll_str = ll_str + str(temp.value)
            temp = temp.next
        print(ll_str)

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for i in range(0, index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.length -1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        temp.value = value
        return temp

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.get(index)
        prev = temp.prev
        next = temp
        new_node = Node(value)
        new_node.prev = prev
        prev.next = new_node
        new_node.next = next
        temp.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.get(index)
        prev = temp.prev
        next = temp.next

        prev.next = next
        next.prev = prev

        temp.prev = None
        temp.next = None

        self.length -= 1
        return True


new_dll = DoubleLinkedList(1)
new_dll.print_list()
new_dll.append(2)
new_dll.append(3)
new_dll.append(4)
new_dll.append(5)
new_dll.print_list()
new_dll.insert(4, 9)
new_dll.print_list()
new_dll.remove(4)
new_dll.print_list()