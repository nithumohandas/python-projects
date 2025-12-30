from double_linked_list import DoubleLinkedList


def reverse(dll: DoubleLinkedList) -> None:
    """Reverses the doubly linked list in-place."""
    current = dll.head
    # Temporary pointer to store the 'prev' during swaps
    # 'prev' will become the new 'next' pointer
    temp_prev = None

    # Iterate through the list
    while current:
        # Swap the next and prev pointers
        temp_prev = current.prev
        current.prev = current.next
        current.next = temp_prev

        # Move to the next node in the original list order.
        # After the swap, the original 'next' is in 'current.prev'
        current = current.prev

    # After the loop, the original 'head' is now the 'tail'
    # The new 'head' is the last node visited, which is the value in temp_prev
    # from the last iteration before current became None
    if temp_prev:
        dll.head = temp_prev.prev  # The last 'prev' stored is the new head


my_dll_1 = DoubleLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(4)
my_dll_1.append(5)

my_dll_1.print_list()