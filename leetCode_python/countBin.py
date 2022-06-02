class Solution:
    def countBits(self, n: int) -> List[int]:
        list=[]
        for i in range(n+1):
            list.append(int([i for i in bin(i)].count('1')))
        return list
            

n=5
o=Solution
print(o.countBits(n))