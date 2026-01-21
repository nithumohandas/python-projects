my_list = [1, 10, 11, 19, 21, 22, 33, 50]

def binary_search(user_list, target):
    left = 0
    right = len(user_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if user_list[mid] == target:
            return mid
        elif target < user_list[mid]:
            right = mid -1
        elif target > user_list[mid]:
            left = mid +1
    return -1

print(binary_search(my_list, 1))