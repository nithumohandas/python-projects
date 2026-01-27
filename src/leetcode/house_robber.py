nums = [2, 7, 9, 3, 1]

def find_max_alt(nums):
    max_returns = []
    max_returns.append(nums[0])
    max_returns.append(max(nums[0], nums[1]))

    for i in range(2, len(nums)):
        max_returns.append(max((max_returns[i-2] + nums[i]), max_returns[i - 1]))

    return max_returns[-1]

print(find_max_alt(nums))

def find_max_robber_2(nums):
    max_skip_first = find_max_alt(nums[1:])
    max_skip_last = find_max_alt(nums[:-1])
    return max(max_skip_first, max_skip_last)

nums = [1,2,3,1]
print(find_max_robber_2(nums))

nums = [2,3,2]
print(find_max_robber_2(nums))