
# Brute Force Approach
def containsDuplicate(nums):
    n = len(nums)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
            
    return False



# Hash Map Approach
def contains_duplicate(nums):
    numMap = {}

    for index, num in enumerate(nums):
        if num in numMap:
            return True
        numMap[num] = index
    
    return False


# Sorting Approach
def contains_Duplicate(nums):
    nums.sort()
    n = len(nums)

    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            return True
        
    return False


# Hash Set Approach
def Contains_Duplicate(nums):

    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False