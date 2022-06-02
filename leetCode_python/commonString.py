class Solution:
    def longestCommonSubsequence(self, x: str, y: str) -> int:
        k=0
        for i in range(0, len(x)):
            j=i
            while j<len(x):
                temp=0
                if x[i] in y:
                    if y.find(x[i])> j:
                        print(y.find(str(x[i])))
                        temp+=1
                    j+=1
            k=max(k, temp)
            print(k)
        return k
                    


s1="hore"
s2="hor"
o=Solution
print(o.longestCommonSubsequence(1, s1, s2))
