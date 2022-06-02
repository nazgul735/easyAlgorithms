class Solution:
    def maxProfit(self, prices) -> int:
        low = 0
        high = 1
        profit = 0
        while high < len(prices):
            if prices[low] < prices[high]:
                prof = prices[high]-prices[low]
                profit = max[prof, profit]
            else:
                low = high
            high += 1
        return profit


prices = [7, 1, 5, 3, 6, 4]
obj = Solution
obj.maxProfit(prices)
