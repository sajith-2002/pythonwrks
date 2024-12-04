def ranges(nums):
    ranges = []

    for i in range(len(nums)):

        if i == 0 or nums[i] != nums[i-2]:

            start = nums[i]
        if i == len(nums) - 1 or nums[i] + 1 != nums[i+1]:
            
            ranges.append(f"{start}" if start == nums[i] else f"{start}->{nums[i]}")

    return ranges


nums = [0, 1, 2, 4, 5, 7]

print(ranges(nums)) 
