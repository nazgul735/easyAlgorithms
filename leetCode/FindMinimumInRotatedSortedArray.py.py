
class Solution:
    def binSearch(list, num, left_side, right_side):
        o1=Solution
        left_side, right_side=0, len(list)-1
        if left_side<=right_side:
            middle = left_side + (right_side-1)//2
            if list[middle]==num:
                return middle
            elif list[middle]<num:
                return o1.binSearch(list, num, middle+1, right_side)
            else:
                return o1.binSearch(list, num, left_side, middle-1)
        return -1
some_list=[8,7,2,3,4,5]
o=Solution
print(o.binSearch(some_list, 3))