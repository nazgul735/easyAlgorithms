class Solution:
    def search(nums, target):
        for i, k in enumerate(nums):
            if i > 0 and k == len(nums)-1:
                continue
            x, j = i+1, len(nums)-1
            while j > x:
                sumThree = k+nums[x]+nums[j]
                i = x+1 if sumThree < target else next
                if sumThree > target:
                    j -= 1
                    continue
                return sumThree
            return 0


nums = [1, 2, 3, 4, 5, 6, 7, 8]
t = 10
o = Solution
print(o.search(nums, t))
