from linked_list import LinkedList, Node


def find_middle_node(test_ll: LinkedList) -> Node:
    slow = test_ll.head
    fast = test_ll.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


ll = LinkedList(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.append(5)
# ll.append(6)

middle = find_middle_node(ll)
print(middle.data)
