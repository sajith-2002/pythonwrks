def closest_to_zero(nums):

    closest=nums[0]

    for num in nums:

        if abs(num)<abs(closest) or (abs(closest)==abs(num) and num>closest ):

            closest=num

    return closest
            
nums=[-3,-2,-1,1,2,3]

result=closest_to_zero(nums)


print("The closest number to 0 is",result)