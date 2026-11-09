from typing import List

def largest_container(heights: List[int]) -> int:
    max_water = 0
    left = 0
    right = len(heights) - 1

    while left < right:
        water = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, water)

        if heights[left] < heights[right]:
            left += 1
        elif heights[right] > heights[left]:
            right -= 1
        else:
            left += 1
            right -= 1
    return max_water


largest_container([2,7,8,3,7,6])