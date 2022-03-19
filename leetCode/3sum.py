class Solution():
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """        
        nums.sort()      
        output = set()
        for k in range(len(nums)):
            target = -nums[k]
            i,j = k+1, len(nums)-1
            while i < j:
                sum_two = nums[i] + nums[j]
                if sum_two < target:
                    i += 1
                elif sum_two > target:
                    j -= 1
                output.add((nums[k],nums[i],nums[j]))
                i += 1
                j -= 1
        return output
