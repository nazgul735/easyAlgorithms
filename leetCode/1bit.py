class Solution:
    def hammingWeight(n: int) -> int:
        return int([i for i in bin(n)].count('1'))
        
n=100000010000000100001
o=Solution
print(o.hammingWeight(n))

