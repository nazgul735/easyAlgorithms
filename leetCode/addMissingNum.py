#assuming only one number is missing
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
    def betterMissingNumber(nums)-> int:
        total=int((len(nums))*(len(nums)+1)/2)
        return int(total-sum(nums))
        
        
n=[3,0,1,2]
o=Solution
# print(o.missingNumber(n))
print(o.betterMissingNumber(n))
        