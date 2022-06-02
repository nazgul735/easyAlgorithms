import numpy
class Solution:
    def productExceptSelf(self, nums):
        prodArr=[]
        totalProd=numpy.prod(nums)
        for i in nums:
            temp=totalProd/i
            prodArr.append(int(temp))
        return prodArr

            
nums=[1,2,3,4]
obj=Solution
print(obj.productExceptSelf(0,nums))