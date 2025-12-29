from typing import Any

from linked_list import LinkedList


def convert_to_decimal(test_ll: LinkedList):
    decimal = 0
    node = test_ll.head
    while node:
        decimal = (decimal * 2) + node.data
        node = node.next
    return decimal

ll = LinkedList(1)
ll.append(0)
ll.append(1)
ll.append(1)
LinkedList.print_list(ll)
# ll.append(0)
# ll.append(1)

decimal = convert_to_decimal(ll)
print(decimal)
