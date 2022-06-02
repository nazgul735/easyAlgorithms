class Solution:
    def maxSubArray(self, nums):
        res = currSum = nums[0]
        for num in nums[1:]:
            currSum = max(currSum + num,  num)
            res = max(res, currSum)
        return res
nums=[-1,1,2,3,4,5,-2,5,-1,2]
obj=Solution
print(obj.maxSubArray(0, nums))

