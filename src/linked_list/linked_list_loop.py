from linked_list import LinkedList, Node


def find_loop(test_ll: LinkedList) -> bool:
    slow = test_ll.head
    fast = test_ll.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow and fast and slow.data == fast.data:
            return True
    return False


my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(find_loop(my_linked_list_1) ) # Returns True




my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(find_loop(my_linked_list_2) ) # Returns False

