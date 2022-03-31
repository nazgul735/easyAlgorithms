class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        prev_2 = 1
        prev_1 = 2
        total = 0
        i = 2
        while i < n:
            total = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = total
            i += 1
        return total
