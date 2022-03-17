class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = round(left + (right-left)/2)

            if nums[middle] < nums[middle-1]:
                return nums[middle]

            elif nums[right] < nums[middle]:
                left = middle+1
            else:
                right = middle-1

        return nums[right]


nums = [1, 2, 3, 4, 5, 6, 7]
o = Solution
print(o.findMin(1, nums))
