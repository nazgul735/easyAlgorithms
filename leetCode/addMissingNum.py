class Solution:
    def missingNumber(nums) -> int:
        nums=sorted(nums)
        if nums[len(nums)-1]!=len(nums):
            return len(nums)
        for i in range(len(nums)):
            if nums[i]==i:
                continue
            if  nums[i]!=i:
                return i
        return None
        
        
n=[3,0,1]
o=Solution
print(o.missingNumber(n))
        