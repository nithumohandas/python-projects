from typing import Any

from linked_list import LinkedList


def remove_dupes(test_ll: LinkedList):
    current = test_ll.head
    while current:
        runner = current
        while runner and runner.next:
            if current.data == runner.next.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(2)
ll.append(3)
ll.append(3)

remove_dupes(ll)
LinkedList.print_list(ll)

