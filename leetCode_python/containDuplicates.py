class Solution:
    def containsDuplicate(nums):
        temp = {}
        for i in nums:
            if i in temp:
                return True
            temp[i] = 1
        return False
