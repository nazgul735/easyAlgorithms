class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        for i in wordDict:
            if i in s:
                wordDict.pop(i)
        return True if len(wordDict) == 0 else False


s = "bildel"
d = ["bil", "del"]
o = Solution
print(o.wordBreak(1, s, d))
