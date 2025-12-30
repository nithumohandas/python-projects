from double_linked_list import DoubleLinkedList

def find_palindrome(dll: DoubleLinkedList) -> bool:
    if dll.length == 1:
        return True
    palindrome = True
    start = dll.head
    end = dll.tail
    while start and end:
        if start.value != end.value:
            palindrome = False
        start = start.next
        end = end.prev
    return palindrome

my_dll_1 = DoubleLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print('my_dll_1 is_palindrome:')
print( find_palindrome(my_dll_1) )


my_dll_2 = DoubleLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print('\nmy_dll_2 is_palindrome:')
print( find_palindrome(my_dll_2) )

my_dll_3 = DoubleLinkedList(1)

print('\nmy_dll_3 is_palindrome:')
print( find_palindrome(my_dll_3) )