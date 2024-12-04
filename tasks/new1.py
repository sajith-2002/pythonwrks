def closest(nums):

    return min(nums, key=lambda x: abs(x))

nums = [-4, -3, 2, 4, 8]
result = closest(nums)
print(result)  