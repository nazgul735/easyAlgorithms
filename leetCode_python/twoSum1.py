def twoSum(nums, t):
    dict = {}
    for i in range(len(nums)):
        dict[nums[i]] = i
    for i in range(len(nums)):
        val = t-nums[i]
        if val in dict and dict[val] == i:
            return i, dict[val]


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
t = 20

print(twoSum(nums, t))
