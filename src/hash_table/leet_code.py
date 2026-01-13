from typing import OrderedDict


def check_anagram(str1, str2):
    str1_dict = {}
    str2_dict = {}
    for char in str1:
        if char not in str1_dict:
            str1_dict[char] = 1
        else:
            str1_dict[char] += 1
    for char in str2:
        if char not in str2_dict:
            str2_dict[char] = 1
        else:
            str2_dict[char] += 1
    print(str1_dict)
    print(str2_dict)
    if str2_dict == str1_dict:
        return True
    return False

print(check_anagram('anagram', 'nagaram'))

def find_duplicates(arr):
    my_dict = {}
    dupes = set()
    for i in arr:
        my_dict[i] = my_dict.get(i, 0) + 1
        if( my_dict.get(i) > 1):
            dupes.add(i)

    return list(dupes)

print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )


def first_non_repeating_char(key):
    my_ord_dict = OrderedDict()
    for char in key:
        my_ord_dict[char] = my_ord_dict.get(char, 0) + 1

    for char in my_ord_dict:
        if my_ord_dict[char] == 1:
            return char

    return None


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )


def group_anagrams(arr):
    anagrams = {}
    for string in arr:
        sorted_str = "".join(sorted(string))
        if sorted_str not in anagrams:
            anagrams[sorted_str] = [string]
        else:
            anagrams[sorted_str].append(string)

    return anagrams.values()


print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )

def two_sum(arr, sum):
    sum_dict = {}
    for i, val in enumerate(arr):
        sum_pair = sum - val
        if sum_pair in sum_dict:
            return [sum_dict[sum_pair], i]
        else:
            sum_dict[val] = i
    return []

print(two_sum([5, 1, 7, 2, 9, 3], 10))
print(two_sum([4, 2, 11, 7, 6, 3], 9))
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
print(two_sum([1, 3, 5, 7, 9], 10))
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )


def subarray_sum(nums, target):
    # Dictionary to store {prefix_sum: index}
    # Initializing with {0: -1} handles subarrays starting from index 0
    prefix_sums = {0: -1}
    current_sum = 0

    for i, num in enumerate(nums):
        current_sum += num

        # Check if (current_sum - target) exists in our hash table
        diff = current_sum - target
        if diff in prefix_sums:
            # Subarray starts after the stored index and ends at current index i
            start_index = prefix_sums[diff] + 1
            return [start_index, i]

        # Store current cumulative sum and its index for future lookups
        # If there are duplicates, this stores the first occurrence (leftmost)
        if current_sum not in prefix_sums:
            prefix_sums[current_sum] = i

    return None  # Return None if no subarray is found


nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )


def remove_duplicates(arr):
    return list(set(arr))

my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
print(new_list)

def find_pairs(arr1, arr2, target):
    pairs = []
    for i in arr1:
        pair = target - i
        if pair in arr2:
            pairs.append([i,pair])

    return pairs


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)


def longest_consecutive_sequence(nums):
    # Convert list to a set for O(1) average-time lookups
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Optimization: Only start a sequence if 'num' is the start of one.
        # If num - 1 is in the set, then 'num' is already part of a sequence
        # started by a smaller number, so we skip it.
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1

            # Keep incrementing while the next consecutive number exists
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1

            # Update the global maximum length found
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )