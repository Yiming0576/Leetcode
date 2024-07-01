
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

def two_sum(nums: list[int], target: int):
    print("Hello, World!")

    map = {}
    for i, num in enumerate(nums):
        if target - num in map:
            return [map[target - num], i]
        map[num] = i

    return []
