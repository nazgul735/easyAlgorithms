class Solution:
    def maxProduct(self, nums):
        output = maxProd = minProd = nums[0]
        for i in nums[1:]:
            candidates = [i, maxProd*i, minProd*i]
            maxProd = max(candidates)
            minProd = min(candidates)
            output = max(output, maxProd)
        return output
