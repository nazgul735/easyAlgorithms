def twoSum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums): 
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []
nums=[1,2,3,4,5,6]
target=9
print(twoSum(None, nums, target))