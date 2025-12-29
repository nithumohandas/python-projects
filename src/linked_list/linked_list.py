class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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
            ll_str = ll_str + str(temp.data)
            temp = temp.next
        print(ll_str)

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        temp_pre = self.head
        for i in range(1, self.length - 1):
            temp_pre = temp_pre.next
        self.tail = temp_pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, data):
        temp = self.get(index)
        temp.data = data
        return temp

    def insert(self, index, data):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(data)
        elif index == self.length:
            return self.append(data)
        else:
            new_node = Node(data)
            temp = self.get(index -1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index < self.length:
            temp = self.get(index - 1)
            removed_index = temp.next
            if index == ( self.length -1):
                temp.next = None
            else:
                temp.next = removed_index.next
                removed_index.next = None
            return removed_index

# new_ll = LinkedList(11)
# new_ll.print_list()
# new_ll.append(22)
# new_ll.pop()
# new_ll.print_list()
# new_ll.append(33)
# new_ll.print_list()
# new_ll.prepend(44)
# new_ll.print_list()
# new_ll.pop_first()
# new_ll.append(55)
# new_ll.print_list()
# print(new_ll.length)
# print(new_ll.get(3))
# new_ll.set_value(3, 55)
# new_ll.print_list()
# new_ll.insert(3, 44)
# new_ll.print_list()