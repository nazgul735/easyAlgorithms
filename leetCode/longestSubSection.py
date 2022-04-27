class Solution:
    def lengthOfLIS(self, nums) -> int:
        
        n=len(nums)
        dp=[1]*(n)
        
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
            
        return max(dp)

nums=[1,2,3,2,3,4,5,6,7]
o=Solution
print(o.lengthOfLIS(1, nums))