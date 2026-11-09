from typing import List


def triplet_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    triplets = []
    for i in range(len(nums) - 1):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] <= 0:
            two_sums = two_number_sum(nums[i + 1:], nums[i])
            if two_sums:
                triplets.extend(two_sums)
    return triplets


def two_number_sum(nums, target):
    right = len(nums) - 1
    left = 0
    triplets = []
    while left < right:

        sum = nums[left] + nums[right] + target

        if sum < 0:
            left += 1
        elif sum > 0:
            right -= 1
        else:
            three_sums = [target, nums[left], nums[right]]
            triplets.append(three_sums)

            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1

    return triplets