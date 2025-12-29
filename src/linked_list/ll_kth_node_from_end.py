from typing import Any

from linked_list import LinkedList, Node

from src.linked_list.linked_list import Node


def kth_node_from_end(test_ll: LinkedList, k: int) -> Any | None:
    slow = fast = test_ll.head

    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next


    while fast:
        slow = slow.next
        fast = fast.next

    return slow


ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
# ll.append(5)
# ll.append(6)

kth_node = kth_node_from_end(ll, 3)
print(kth_node.data)
