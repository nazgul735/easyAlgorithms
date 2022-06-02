class Solution:
    def coinChange(coins, amount: int) -> int:
        if amount in coins:
            return 1
        if amount == 0:
            return 0
        tot=0
        remaining=amount
        coins=sorted(coins)
        for i in coins[::-1]:
            if i>remaining:
                continue
            temp=i*(remaining//i)
            remaining-=temp
            tot+=int(temp/i)
        return tot if remaining==0 else -1
    





coins=[186,419,83,408]
amount=6249
o=Solution
print(o.coinChange(coins, amount))
