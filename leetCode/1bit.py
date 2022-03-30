class Solution:
    def hammingWeight(n: int) -> int:
        return int([i for i in bin(n)].count('1'))
        
n=3
o=Solution
print(o.hammingWeight(n))

