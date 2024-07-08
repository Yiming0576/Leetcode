
# # Brute Force Approach
def two_sum(nums, target):

    n = len(nums)

    for i in range(n - 1):
        for j in range(i + 1, n):
            
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return [] # No solution found

result =  two_sum([2, 7, 11, 15], 9)
print(result)



# Hash Map Approach
def twoSum(nums, target):

    numMap = {}
    n = len(nums)

    # store the nums into the numMap
    for i in range(n):
        numMap[nums[i]] = i

    
    # Find the complement
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]
        
    return [] # No solution found

# Hash Map Approach wiht one Map
def two_sum(nums, target):
    
    numMap = {}
    n = len(nums)


    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i ]
        numMap[nums[i]] = i
    
    return [] # No solution found


