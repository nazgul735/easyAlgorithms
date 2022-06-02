import bisect


class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = []
        for n in nums:
            i = bisect.bisect(dp, n)
            if dp and dp[i - 1] == n:
                continue
            if i == len(dp):
                dp.append(n)
            else:
                dp[i] = n
        return len(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18, 200]
o = Solution
print(o.lengthOfLIS(1, nums))
