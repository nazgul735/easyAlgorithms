class Solution:
    def reverseBits(n: int) -> int:
        return int(f'{n:032b}'[::-1], 2)

    def secondReverseBits(n):
        r = 0
        for i in range(32):
            r |= (n >> i & 1) << 31 - i
        return r


n = 1001100001111
o = Solution
print(o.reverseBits(n))
