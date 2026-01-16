nums = [1, 1, 1, 2, 2, 2, 2, 3, 4, 5, 5, 6, 5, 5]
k = 2

def kth_largest(nums, k):
    num_map = {}
    for num in nums:
        if num not in num_map:
            num_map[num] = 1
        else:
            num_map[num] += 1

    # Two ways to find kth largest
    # 1 - Sort reverse of dict by value

    rev_sorted_map = {k: v for k, v in sorted(num_map.items(), key=lambda item: item[1], reverse=True)}
    kth_largest = []
    for n,v in rev_sorted_map.items():
        if len(kth_largest) < k:
            kth_largest.append(n)
        else:
            break
    print(kth_largest)

kth_largest(nums, k)